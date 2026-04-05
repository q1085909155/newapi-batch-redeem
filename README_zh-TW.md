[简体中文](README.md) | **繁體中文** | [English](README_en.md)

# NewAPI 批量兌換碼工具

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/依賴-無-brightgreen.svg)]()

一個輕量級的 Python 命令列工具，用於批量兌換 [NewAPI](https://github.com/Calcium-Ion/new-api)（new-api / one-api）平台的兌換碼。零依賴，僅使用 Python 標準庫。

## ✨ 功能特點

- 📦 **批量兌換** — 從檔案批量讀取兌換碼並自動兌換
- ⏱️ **頻率控制** — 可自訂兌換間隔，防止請求過快被限流
- 📝 **結果記錄** — 自動生成詳細結果報告
- 🔒 **SSL 相容** — 自動處理自簽名證書
- 🖥️ **背景執行** — 支援非互動式無人值守執行
- 🚀 **零依賴** — 僅依賴 Python 標準庫

## 📋 環境需求

- Python 3.6+

## 🚀 快速開始

### 1. 複製儲存庫

```bash
git clone https://github.com/q1085909155/newapi-batch-redeem.git
cd newapi-batch-redeem
```

### 2. 準備兌換碼

建立 `codes.txt` 檔案，每行一個兌換碼：

```
abc123def456
xyz789ghi012
...
```

以 `#` 開頭的行為註解，會被忽略。

### 3. 執行

**互動式執行（會提示輸入參數）：**

```bash
python batch_redeem.py
```

**命令列模式（推薦）：**

```bash
python batch_redeem.py --url https://你的NewAPI地址 --token 你的存取令牌 --user 你的使用者ID --file codes.txt -y
```

**完整參數範例：**

```bash
python batch_redeem.py \
  --url https://your-newapi-site.com \
  --token your_access_token \
  --user your_user_id \
  --file codes.txt \
  --delay 180 \
  -y
```

## ⚙️ 參數說明

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `--url` | NewAPI 站點地址 | *（必填）* |
| `--token` | 存取令牌（在個人設定中取得） | *（必填）* |
| `--user` | 使用者ID（`New-Api-User` 請求標頭） | *（可選）* |
| `--file` | 兌換碼檔案路徑 | `codes.txt` |
| `--delay` | 每次兌換間隔秒數 | `180`（3分鐘） |
| `-y` / `--yes` | 跳過確認提示 | 否 |

## 🔑 如何取得 Token

1. 登入 NewAPI 網站
2. 進入「個人設定」頁面
3. 複製「系統存取令牌」

> ⚠️ **注意**：使用「系統存取令牌」，不是 `sk-` 開頭的 API Key。

## 📄 輸出結果

兌換完成後，結果儲存在 `redeem_results.txt`。

## 🤝 相容平台

- [new-api](https://github.com/Calcium-Ion/new-api)
- [one-api](https://github.com/songquanpeng/one-api)（可能相容，未完全測試）
- 其他基於 new-api 的 API 管理平台

## 📜 授權條款

Apache License 2.0

## ⭐ Star

如果這個工具對你有幫助，請點個 Star！⭐
