# Try Code Project

這是一個包含多種編程語言和應用的測試項目。

## 項目內容

### 🎮 2048 遊戲
- **文件**: `2048.html`
- **描述**: 經典的2048滑動拼圖遊戲的HTML實現
- **使用方法**: 在瀏覽器中打開`2048.html`即可遊玩

### ☕ Java 測試程序
- **文件**: `SimpleTest.java` / `SimpleTest.class`
- **描述**: 簡單的Java測試程序，輸出Hello World並計算1到10的總和
- **運行方法**: 
  ```bash
  java SimpleTest
  ```

### 🐍 Python 性能基準測試
- **文件**: `benchmark_m2_m4.py`
- **描述**: M2和M4 CPU性能基準測試腳本
- **功能**:
  - 斐波那契序列計算（測試單核CPU性能）
  - 大型矩陣乘法（測試向量化和多核性能）
  - 系統信息顯示
- **運行方法**:
  ```bash
  python benchmark_m2_m4.py
  ```

### 🤖 Claude AI 代理配置
- **目錄**: `.claude/agents/`
- **內容**: 包含多個AI代理的配置文件
  - `code-reviewer.md` - 代碼審查代理
  - `debugger.md` - 調試代理
  - `fullstack-developer.md` - 全棧開發代理

## 技術棧

- **前端**: HTML, CSS, JavaScript
- **後端**: Java
- **腳本**: Python
- **工具**: NumPy, SciPy

## 系統要求

- **2048遊戲**: 支持HTML5的現代瀏覽器
- **Java程序**: JDK 8 或更高版本
- **Python腳本**: Python 3.x + NumPy + SciPy

## 快速開始

1. 克隆倉庫:
   ```bash
   git clone <repository-url>
   cd try-code
   ```

2. 運行2048遊戲:
   ```bash
   open 2048.html  # macOS
   # 或在瀏覽器中直接打開該文件
   ```

3. 編譯並運行Java程序:
   ```bash
   javac SimpleTest.java
   java SimpleTest
   ```

4. 運行性能基準測試:
   ```bash
   pip install numpy scipy
   python benchmark_m2_m4.py
   ```

## 作者

Kit

## 許可證

此項目僅用於學習和測試目的。