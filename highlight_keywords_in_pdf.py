import fitz  # PyMuPDF 的模組名稱

def highlight_keywords_in_pdf(input_pdf, output_pdf, keywords):
    """
    在 PDF 中搜尋關鍵字並加上黃色螢光筆標註
    """
    # 1. 開啟 PDF
    doc = fitz.open(input_pdf)
    
    # 記錄標註了多少處
    count = 0

    # 2. 遍歷每一頁
    for page in doc:
        for word in keywords:
            # 3. 搜尋文字，這會回傳所有該文字出現的座標區域 (Rects)
            # quad 支援旋轉文字，一般情況用 search_for 即可
            text_instances = page.search_for(word)
            
            # 4. 對每一個找到的實例加上標註
            for inst in text_instances:
                # Add highlight annotation (預設是黃色)
                highlight = page.add_highlight_annot(inst)
                highlight.update() # 儲存標註狀態
                count += 1

    # 5. 存檔
    doc.save(output_pdf)
    print(f"完成！共標註了 {count} 處關鍵字，檔案已儲存為：{output_pdf}")

# --- 使用範例 ---
source_file = "my_document.pdf"       # 你的來源 PDF
target_file = "highlighted_doc.pdf"   # 輸出的 PDF
summary_keywords = ["人工智慧", "營收成長", "風險評估"] # 從摘要中提取的重點文字

# 執行函式 (請確保資料夾中有 my_document.pdf 檔案以免報錯)
# highlight_keywords_in_pdf(source_file, target_file, summary_keywords)
