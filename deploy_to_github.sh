#!/bin/bash

# 获取当前脚本所在目录
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/toefl-course-web"

echo "========================================================"
echo "   GitHub Pages 自动部署助手 (Auto Deploy Helper)"
echo "========================================================"
echo ""
echo "1. 请确保你已经登录 GitHub 并创建了一个新的空仓库 (Public)."
echo "   (我已经帮你打开了 https://github.com/new)"
echo ""
echo "2. 请将新仓库的 HTTPS 地址粘贴在下面"
echo "   (格式例如: https://github.com/username/repo-name.git)"
echo ""
echo -n "请输入仓库链接: "
read REPO_URL

if [ -z "$REPO_URL" ]; then
  echo "错误: 未输入链接。"
  exit 1
fi

echo ""
echo "正在配置远程仓库..."
git remote remove origin 2>/dev/null # 移除可能存在的旧 origin
git remote add origin "$REPO_URL"

echo "正在推送代码到 GitHub..."
echo "注意: 如果是第一次连接，可能需要输入 GitHub 的账号密码或 Token。"
git branch -M main
git push -u origin main

echo ""
echo "========================================================"
echo "   ✅ 代码推送成功！"
echo "========================================================"
echo "最后一步："
echo "1. 回到 GitHub 仓库页面。"
echo "2. 点击 'Settings' (设置) -> 左侧 'Pages'。"
echo "3. 在 'Source' 下选择 'Deploy from a branch'。"
echo "4. Branch 选择 'main'，文件夹 '/(root)'，点击 Save。"
echo "5. 等待 1 分钟刷新，即可看到你的网页链接！"
