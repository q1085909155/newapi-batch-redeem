[简体中文](README.md) | [繁體中文](README_zh-TW.md) | **English**

# NewAPI Batch Redemption Tool

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen.svg)]()

A lightweight Python CLI tool for batch redeeming codes on [NewAPI](https://github.com/Calcium-Ion/new-api) (new-api / one-api) platforms. Zero dependencies — uses only Python standard library.

## ✨ Features

- 📦 **Batch Redeem** — Read codes from file and redeem automatically
- ⏱️ **Rate Limiting** — Configurable delay between requests
- 📝 **Result Logging** — Auto-generate detailed result report
- 🔒 **SSL Compatible** — Handles self-signed certificates
- 🖥️ **Non-interactive Mode** — Run unattended in background
- 🚀 **Zero Dependencies** — Python standard library only

## 📋 Requirements

- Python 3.6+

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/q1085909155/newapi-batch-redeem.git
cd newapi-batch-redeem
```

### 2. Prepare codes

Create a `codes.txt` file with one code per line:

```
abc123def456
xyz789ghi012
...
```

Lines starting with `#` are comments and will be ignored.

### 3. Run

**Interactive mode:**

```bash
python batch_redeem.py
```

**Command line mode (recommended):**

```bash
python batch_redeem.py --url https://your-newapi-site.com --token YOUR_TOKEN --user YOUR_USER_ID --file codes.txt -y
```

**Full example:**

```bash
python batch_redeem.py \
  --url https://your-newapi-site.com \
  --token your_access_token \
  --user your_user_id \
  --file codes.txt \
  --delay 180 \
  -y
```

## ⚙️ Options

| Option | Description | Default |
|--------|-------------|---------|
| `--url` | NewAPI site URL | *(required)* |
| `--token` | Access token (from personal settings) | *(required)* |
| `--user` | User ID (`New-Api-User` header) | *(optional)* |
| `--file` | Path to codes file | `codes.txt` |
| `--delay` | Delay between requests (seconds) | `180` (3 min) |
| `-y` / `--yes` | Skip confirmation | `false` |

## 🔑 How to get your Token

1. Log in to the NewAPI website
2. Go to **Personal Settings**
3. Copy your **System Access Token**

> ⚠️ **Note**: Use the "System Access Token", NOT the API Key (which starts with `sk-`).

## 📄 Output

After completion, results are saved to `redeem_results.txt`.

## 🤝 Compatible Platforms

- [new-api](https://github.com/Calcium-Ion/new-api)
- [one-api](https://github.com/songquanpeng/one-api) (may work, not fully tested)
- Other API management platforms based on new-api

## 📜 License

Apache License 2.0

## ⭐ Star

If this tool helps you, please give it a star! ⭐
