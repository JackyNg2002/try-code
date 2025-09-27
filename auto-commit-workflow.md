# 自動 Commit & Push 工作流程

## 你提供給我的信息：
1. 倉庫 URL 或目錄路徑
2. (可選) 提交信息描述

## 我會自動執行：

### 第一步：分析更改
```bash
git status                    # 檢查更改狀態
git diff                     # 查看具體更改
```

### 第二步：智能提交
```bash
git add .                    # 添加所有更改
git commit -m "智能生成的提交信息"  # 基於更改內容
```

### 第三步：推送更新
```bash
git push                     # 推送到 GitHub
```

### 第四步：確認完成
```bash
git log --oneline -1         # 顯示最新提交
git status                   # 確認工作目錄乾淨
```

## 示例場景：

### 場景1：你修改了代碼
- 你：「我更新了 app.js 修復了一個 bug」
- 我：自動 commit "Fix bug in app.js" + push

### 場景2：你添加了新功能  
- 你：「我添加了用戶登錄功能」
- 我：自動 commit "Add user login feature" + push

### 場景3：你想批量更新
- 你：「幫我提交所有更改」
- 我：分析所有更改 + 生成描述 + commit + push