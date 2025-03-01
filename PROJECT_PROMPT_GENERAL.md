**Denki-Mate: 親子互動電子寵物**

核心概念：
- 結合 IoT 設備與手機應用的電子寵物培養系統
- 透過實體設備（M5StickC PLUS）展示寵物
- 手機 App 用於家長端控制與互動
- 專注於親子互動與獎勵機制

技術堆疊：
1. 硬體
- M5StickC PLUS/PLUS2 (ESP32 based)
- 內建 LCD 顯示器、按鈕、LED、震動
- 內建 WiFi/藍牙連接

2. 移動應用
- Flutter 跨平台開發
- 藍牙/WiFi 連接管理
- 家長控制介面

3. 後端服務
- Golang 開發
- 基本的資料同步
- 安全的通訊協議

主要功能：
1. 基礎寵物系統
- 寵物狀態顯示
- 餵食與互動機制
- 情緒回饋系統

2. 獎勵機制
- 家長設定任務
- 完成任務獲得獎勵
- 寵物成長系統

3. 親子互動
- 即時狀態同步
- 互動歷史記錄
- 成就系統

發展方向：
1. 以家庭使用為起點
2. 透過實際使用回饋改進
3. 注重親子互動體驗
4. 符合兒童使用安全規範

這個專案的特色是從實際親子需求出發，強調實體互動，並能根據使用經驗持續優化。