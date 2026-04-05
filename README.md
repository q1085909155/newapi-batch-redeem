# NewAPI Batch Redemption Tool / NewAPI 批量兑换码工具

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen.svg)]()

A lightweight Python CLI tool for batch redeeming codes on [NewAPI](https://github.com/Calcium-Ion/new-api) (new-api / one-api) platforms. Zero dependencies — uses only Python standard library.

一个轻量级的 Python 命令行工具，用于批量兑换 [NewAPI](https://github.com/Calcium-Ion/new-api)（new-api / one-api）平台的兑换码。零依赖，仅使用 Python 标准库。

## ✨ Features / 功能特点

- 📦 **Batch Redeem** — Read codes from file and redeem automatically / 从文件批量读取兑换码并自动兑换
- ⏱️ **Rate Limiting** — Configurable delay between requests / 可自定义兑换间隔，防止请求过快
- 📝 **Result Logging** — Auto-generate detailed result report / 自动生成详细结果报告
- 🔒 **SSL Compatible** — Handles self-signed certificates / 自动处理自签名证书
- 🖥️ **Non-interactive Mode** — Run unattended in background / 支持后台无人值守运行
- 🚀 **Zero Dependencies** — Python standard library only / 仅依赖 Python 标准库

## 📋 Requirements / 环境要求

- Python 3.6+

## 🚀 Quick Start / 快速开始

### 1. Clone this repository / 克隆仓库

```bash
git clone https://github.com/q1085909155/newapi-batch-redeem.git
cd newapi-batch-redeem
```

### 2. Prepare your codes / 准备兑换码

Create a `codes.txt` file with one code per line:

创建 `codes.txt` 文件，每行一个兑换码：

```
abc123def456
xyz789ghi012
...
```

Lines starting with `#` are treated as comments and will be ignored.

以 `#` 开头的行为注释，会被忽略。

### 3. Run / 运行

**Interactive mode (prompts for input) / 交互式运行：**

```bash
python batch_redeem.py
```

**Command line mode (recommended) / 命令行模式（推荐）：**

```bash
python batch_redeem.py --url https://your-newapi-site.com --token YOUR_ACCESS_TOKEN --file codes.txt -y
```

**Full example with all options / 完整参数示例：**

```bash
python batch_redeem.py \
  --url https://your-newapi-site.com \
  --token your_access_token \
  --user your_user_id \
  --file codes.txt \
  --delay 180 \
  -y
```

## ⚙️ Options / 参数说明

| Option | Description | Default |
|--------|-------------|---------|
| `--url` | NewAPI site URL / 站点地址 | *(required)* |
| `--token` | Access token (from personal settings) / 访问令牌 | *(required)* |
| `--user` | User ID (`New-Api-User` header) / 用户ID | *(optional)* |
| `--file` | Path to codes file / 兑换码文件路径 | `codes.txt` |
| `--delay` | Delay between requests (seconds) / 间隔秒数 | `180` (3 min) |
| `-y` / `--yes` | Skip confirmation / 跳过确认 | `false` |

## 🔑 How to get your Token / 如何获取 Token

1. Log in to the NewAPI website / 登录 NewAPI 网站
2. Go to **Personal Settings** / 进入「个人设置」页面
3. Copy your **System Access Token** / 复制「系统访问令牌」

> ⚠️ **Note**: Use the "System Access Token", NOT the API Key (which starts with `sk-`).
>
> ⚠️ **注意**：使用「系统访问令牌」，不是 `sk-` 开头的 API Key。

## 📄 Output / 输出

After completion, results are saved to `redeem_results.txt`:

兑换完成后，结果保存在 `redeem_results.txt`：

```
Redemption Results - 2024-01-01 12:00:00
Target: https://your-newapi-site.com
Success: 15 | Failed: 4 | Total: 19
============================================================

[OK] abc123def456 - Redeemed successfully
[FAIL] xyz789ghi012 - Code already used
...
```

## 🤝 Compatible Platforms / 兼容平台

- [new-api](https://github.com/Calcium-Ion/new-api)
- [one-api](https://github.com/songquanpeng/one-api) (may work, not fully tested)
- Other OpenAI API management platforms based on new-api / 其他基于 new-api 的 API 管理平台

## 📜 License

MIT

## ⭐ Star History

If this tool helps you, please give it a star! ⭐

如果这个工具对你有帮助，请点个 Star！⭐
