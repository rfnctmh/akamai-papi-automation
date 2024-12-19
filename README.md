# Akamai PAPI 自動化操作
此儲存庫提供了一系列 Python 腳本與設定檔範本，用於管理和自動化 Akamai Property Manager API (PAPI) 的相關操作。工作流程涵蓋屬性修改、規則樹更新、版本部署，以及測試與生產環境的操作。

## 功能特色
- 建立與管理 Akamai PAPI 的 API 憑證。
- 使用 Python 自動化屬性版本的建立與部署。
- 下載、編輯、驗證規則樹的內容。
- 查詢站台相關資訊，例如屬性 ID。
- 推送屬性更新至測試與生產環境。
- 記錄並管理操作過程中的警告與錯誤。

## 使用前準備
### 1. 安裝必要工具：
   - Python 3.x
   - Visual Studio Code（需安裝 Property Manager 插件）
   - 在 Windows 上安裝 WSL 以使用 Linux 工具
### 2. 安裝 EdgeGrid Authentication 套件：
```
pip install edgegrid-python
```

## 使用方法
### 1. 設定 API 憑證
將 .edgerc.example 複製為 .edgerc。
```
client_secret = <YOUR_CLIENT_SECRET>
host = <YOUR_HOST>
access_token = <YOUR_ACCESS_TOKEN>
client_token = <YOUR_CLIENT_TOKEN>
```
### 2. 執行腳本
- 取得屬性詳情與站台相關的 ID 資訊
- 執行腳本以查詢站台屬性資訊（如屬性 ID）：
```
python scripts/get_property_details.py
```
此腳本將返回屬性列表及其相關的 ID 和版本資訊，供後續操作參考。
#### 建立新版本
執行腳本為屬性創建新版本：
```
python scripts/create_new_property.py
```
該腳本會根據當前屬性的版本建立新版本，並返回新版本的相關資訊（如版本號）。
#### 列出屬性版本
列出屬性所有版本及相關的版本資訊：
```
python scripts/list_property_versions.py
```
#### 下載規則樹
下載屬性的規則樹至本地：
```
python scripts/get_property_rule_tree.py
```
#### 更新規則樹
對規則樹進行修改後，執行腳本更新：
```
python scripts/update_property_rule_tree.py
```
### 3. 部署修改
- 推送至測試環境
- 執行腳本將修改推送至測試環境：
```
python scripts/deploy_to_staging.py
```
- 推送至生產環境
- 測試完成後，執行腳本部署至生產環境：
```
python scripts/deploy_to_production.py
```

## 注意事項
- 驗證規則樹變更：在提交更新之前，務必使用 dryRun: true 驗證規則樹的變更，以確保更新無誤。
- 白名單設置：確保您的 IP 已被列入 Akamai API 的白名單，否則可能導致請求失敗。
- 錯誤管理：若發現警告或錯誤，請參考日誌記錄進行修正後重試。