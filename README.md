**简体中文** | [繁體中文](README_zh-TW.md) | [English](README_en.md)

# NewAPI 批量兑换码工具

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![No Dependencies](https://img.shields.io/badge/依赖-无-brightgreen.svg)]()

一个轻量级的 Python 命令行工具，用于批量兑换 [NewAPI](https://github.com/Calcium-Ion/new-api)（new-api / one-api）平台的兑换码。零依赖，仅使用 Python 标准库。

## ✨ 功能特点

- 📦 **批量兑换** — 从文件批量读取兑换码并自动兑换
- ⏱️ **频率控制** — 可自定义兑换间隔，防止请求过快被限流
- 📝 **结果记录** — 自动生成详细结果报告
- 🔒 **SSL 兼容** — 自动处理自签名证书
- 🖥️ **后台运行** — 支持非交互式无人值守运行
- 🚀 **零依赖** — 仅依赖 Python 标准库

## 📋 环境要求

- Python 3.6+

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/q1085909155/newapi-batch-redeem.git
cd newapi-batch-redeem
```

### 2. 准备兑换码

创建 `codes.txt` 文件，每行一个兑换码：

```
abc123def456
xyz789ghi012
...
```

以 `#` 开头的行为注释，会被忽略。

### 3. 运行

**交互式运行（会提示输入参数）：**

```bash
python batch_redeem.py
```

**命令行模式（推荐）：**

```bash
python batch_redeem.py --url https://你的NewAPI地址 --token 你的访问令牌 --user 你的用户ID --file codes.txt -y
```

**完整参数示例：**

```bash
python batch_redeem.py \
  --url https://your-newapi-site.com \
  --token your_access_token \
  --user your_user_id \
  --file codes.txt \
  --delay 180 \
  -y
```

## ⚙️ 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--url` | NewAPI 站点地址 | *（必填）* |
| `--token` | 访问令牌（在个人设置中获取） | *（必填）* |
| `--user` | 用户ID（`New-Api-User` 请求头） | *（可选）* |
| `--file` | 兑换码文件路径 | `codes.txt` |
| `--delay` | 每次兑换间隔秒数 | `180`（3分钟） |
| `-y` / `--yes` | 跳过确认提示 | 否 |

## 🔑 如何获取 Token

1. 登录 NewAPI 网站
2. 进入「个人设置」页面
3. 复制「系统访问令牌」

> ⚠️ **注意**：使用「系统访问令牌」，不是 `sk-` 开头的 API Key。

## 📄 输出结果

兑换完成后，结果保存在 `redeem_results.txt`：

```
Redemption Results - 2024-01-01 12:00:00
Target: https://your-newapi-site.com
Success: 15 | Failed: 4 | Total: 19
============================================================

[OK] abc123def456 - 兑换成功
[FAIL] xyz789ghi012 - 兑换码已被使用
...
```

## 🤝 兼容平台

- [new-api](https://github.com/Calcium-Ion/new-api)
- [one-api](https://github.com/songquanpeng/one-api)（可能兼容，未完全测试）
- 其他基于 new-api 的 API 管理平台

## 📜 许可证

Apache License 2.0

## ⭐ Star

如果这个工具对你有帮助，请点个 Star！⭐
