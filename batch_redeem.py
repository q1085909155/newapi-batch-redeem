"""
NewAPI Batch Redemption Code Tool / NewAPI 批量兑换码工具

Batch redeem codes for NewAPI (new-api) platform.
批量兑换 NewAPI 平台的兑换码。

Usage / 使用方法:
  1. Put redemption codes in codes.txt, one per line
     将兑换码放入 codes.txt 文件中，每行一个
  2. Run: python batch_redeem.py
     运行: python batch_redeem.py
  3. Follow prompts to enter NewAPI URL and Token
     按提示输入 NewAPI 地址和用户 Token

  Or use command line arguments / 或直接通过命令行参数:
  python batch_redeem.py --url https://your-newapi-site.com --token YOUR_TOKEN --file codes.txt -y
"""

import urllib.request
import urllib.error
import json
import sys
import time
import argparse
import os
import ssl


# Create SSL context that skips certificate verification
# 创建忽略 SSL 验证的上下文（兼容自签名证书）
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


def redeem_code(base_url, token, code, user_id=""):
    """
    Redeem a single code via NewAPI /api/user/topup endpoint.
    兑换单个兑换码。
    """
    url = f"{base_url.rstrip('/')}/api/user/topup"

    data = json.dumps({"key": code}).encode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    if user_id:
        headers["New-Api-User"] = user_id

    req = urllib.request.Request(url, data=data, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=30, context=ssl_context) as resp:
            raw = resp.read().decode("utf-8")
            try:
                result = json.loads(raw)
            except json.JSONDecodeError:
                return {"success": False, "message": f"Non-JSON response: {raw[:200]}"}
            return {
                "_raw": result,
                "success": result.get("success", False),
                "message": result.get("message", result.get("msg", str(result))),
            }
    except urllib.error.HTTPError as e:
        try:
            error_raw = e.read().decode("utf-8")
            error_body = json.loads(error_raw)
            return {
                "success": False,
                "message": error_body.get("message", error_body.get("msg", str(error_body))),
            }
        except Exception:
            return {"success": False, "message": f"HTTP {e.code}: {e.reason}"}
    except urllib.error.URLError as e:
        return {"success": False, "message": f"Connection error: {e.reason}"}
    except Exception as e:
        return {"success": False, "message": f"Exception: {type(e).__name__}: {str(e)}"}


def load_codes_from_file(filepath):
    """
    Load redemption codes from a text file, one code per line.
    从文本文件加载兑换码，每行一个。
    """
    if not os.path.exists(filepath):
        print(f"[Error] File not found: {filepath}")
        return []

    codes = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            code = line.strip()
            if code and not code.startswith("#"):
                codes.append(code)
    return codes


def main():
    parser = argparse.ArgumentParser(
        description="NewAPI Batch Redemption Code Tool / NewAPI 批量兑换码工具"
    )
    parser.add_argument(
        "--url", type=str, help="NewAPI site URL (e.g. https://your-newapi-site.com)"
    )
    parser.add_argument(
        "--token", type=str, help="Your access token (from NewAPI personal settings)"
    )
    parser.add_argument(
        "--user", type=str, help="Your user ID (New-Api-User header, optional)"
    )
    parser.add_argument(
        "--file",
        type=str,
        default="codes.txt",
        help="Path to redemption codes file (default: codes.txt)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=180,
        help="Delay in seconds between each redemption (default: 180 = 3 minutes)",
    )
    parser.add_argument(
        "-y",
        "--yes",
        action="store_true",
        help="Skip confirmation prompt, start immediately",
    )

    args = parser.parse_args()

    # Get URL
    base_url = args.url
    if not base_url:
        base_url = input(
            "Enter NewAPI URL (e.g. https://your-newapi-site.com): "
        ).strip()
    if not base_url:
        print("[Error] NewAPI URL is required")
        sys.exit(1)

    # Get Token
    token = args.token
    if not token:
        token = input("Enter your access token: ").strip()
    if not token:
        print("[Error] Access token is required")
        sys.exit(1)

    # Get User ID (optional)
    user_id = args.user
    if not user_id:
        try:
            user_id = input(
                "Enter your user ID (New-Api-User, press Enter to skip): "
            ).strip()
        except EOFError:
            user_id = ""

    # Load codes
    codes_file = args.file
    codes = load_codes_from_file(codes_file)

    if not codes:
        print(
            f"[Error] No codes found. Make sure {codes_file} exists and contains codes (one per line)"
        )
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  NewAPI Batch Redemption Tool")
    print(f"{'='*60}")
    print(f"  Target URL : {base_url}")
    print(f"  Code count : {len(codes)}")
    print(f"  Delay      : {args.delay}s")
    print(f"{'='*60}\n")

    # Confirm
    if not args.yes:
        try:
            confirm = input("Start redemption? (y/n): ").strip().lower()
            if confirm not in ("y", "yes"):
                print("Cancelled.")
                sys.exit(0)
        except EOFError:
            print("[Info] Non-interactive mode detected, proceeding automatically...")

    print()

    success_count = 0
    fail_count = 0
    results = []

    for i, code in enumerate(codes, 1):
        # Mask code for display
        if len(code) > 8:
            display_code = code[:4] + "****" + code[-4:]
        else:
            display_code = code[:2] + "****"

        print(f"[{i}/{len(codes)}] Redeeming: {display_code} ... ", end="", flush=True)

        result = redeem_code(base_url, token, code, user_id)

        if result.get("success"):
            success_count += 1
            message = result.get("message", "OK")
            print(f"✓ Success - {message}")
        else:
            fail_count += 1
            message = result.get("message", "Unknown error")
            print(f"✗ Failed - {message}")

        results.append(
            {
                "code": code,
                "success": result.get("success", False),
                "message": message,
            }
        )

        # Delay between requests
        if i < len(codes):
            remaining = len(codes) - i
            next_time = time.strftime(
                "%H:%M:%S", time.localtime(time.time() + args.delay)
            )
            print(
                f"    Waiting {args.delay}s (next at {next_time}, {remaining} remaining)..."
            )
            time.sleep(args.delay)

    # Summary
    print(f"\n{'='*60}")
    print(f"  Done!")
    print(f"  Success: {success_count}  |  Failed: {fail_count}  |  Total: {len(codes)}")
    print(f"{'='*60}")

    # Save results
    result_file = "redeem_results.txt"
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(f"Redemption Results - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Target: {base_url}\n")
        f.write(f"Success: {success_count} | Failed: {fail_count} | Total: {len(codes)}\n")
        f.write(f"{'='*60}\n\n")
        for r in results:
            status = "OK" if r["success"] else "FAIL"
            f.write(f"[{status}] {r['code']} - {r['message']}\n")

    print(f"\nDetailed results saved to: {result_file}")


if __name__ == "__main__":
    main()
