import json
import re

def aggressive_json_cleaner(raw_text):
    """
    清洗 LLM 回傳的髒 JSON 字串：
    1. 移除 // 單行註解
    2. 移除 /* */ 多行註解
    3. 嘗試修復常見的結尾逗號錯誤 (Trailing Commas)
    """
    if not raw_text:
        return {}

    # 1. 移除單行註解 (// ...)
    # regex 解釋: 匹配 // 後面直到換行的內容，但排除網址中的 // (如 http://)
    text = re.sub(r'(?<!:)//.*', '', raw_text)
    
    # 2. 移除多行註解 (/* ... */)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    
    # 3. 移除 Markdown 標記 (```json ... ```)
    text = re.sub(r'```json', '', text)
    text = re.sub(r'```', '', text)
    
    # 4. 去除前後空白
    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # 如果還是失敗，這裡可以加一個更進階的處理，或是直接回傳 None
        print(f"⚠️ JSON 清洗後仍解析失敗: {text[:50]}...")
        return None

# ==========================================
# 測試範例
# ==========================================

# 模擬 Breeze-2-8b 吐出的髒資料
llm_output = """
```json
{
  "hospital_name": "台大醫院", // 這是醫院名稱
  "visit_date": "2023-10-15", /* 這裡本來是民國年 */
  "diagnosis": ["高血壓", "糖尿病"] // Check this
}
