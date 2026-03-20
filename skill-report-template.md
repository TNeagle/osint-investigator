# OSINT Report Template — 情報報告模板

> **Load this file during Phase 6 (Reporting).**
> See SKILL.md for when to invoke.

## Template

```markdown
# OSINT 情報調查報告
> **語言規定**：本報告全文使用**繁體中文**撰寫。

## 執行摘要（Executive Summary）
[2-3句話：核心發現與重要性]

## 調查需求（Intelligence Requirement）
[用戶希望了解的問題]

## 主要發現（Key Findings）
### 發現一：[標題]
- **信心等級**：[高／中／低／推測]
- **信心依據**：[使用的來源類型；反向驗證結果]
- **摘要**：[發現內容]
- **證據鏈**：[附帶 inline confidence tag 的編號步驟]
- **反向驗證搜尋**：[執行的查詢；發現或未發現的反證]
- **替代解釋**：[若有]

## 時間軸（Timeline）
[按時間順序重建事件，如適用]

## 關係網絡圖（Network Map）
[NetworkX 圖表視覺化 + 關鍵指標]

## 🔴 多輪洞察分析（Multi-Round Insight Analysis）

### Round 1 發現 — 模式與異常
[由Round 1 Agent產出：矛盾信號、結構異常、時間序列模式、缺失實體]
[每個洞察必須包含完整推理鏈]

### Round 2 發現 — 矛盾解析與二階推論
[由Round 2 Agent產出：矛盾統一解釋、二階推論、風險層級、金絲雀指標]
[每個洞察必須追溯到Round 1的哪個發現]

### Round 3 發現 — 戰略綜合（複雜調查）
[由Round 3 Agent產出：完整推理鏈、情境矩陣、資訊價值分析、元分析]
[每個建議必須有從原始數據到結論的完整鏈條]

### 推理鏈索引
[編號列出所有主要推理鏈，格式：]
| 鏈# | 起點（數據） | 中間推論 | 終點（結論） | 來源輪次 | 信心 |
|-----|------------|---------|------------|---------|------|
| 1 | [原始觀察] | [A→B→C] | [戰略建議] | R1/R2/R3 | 高/中/低 |

## 投資建議 — 雙軌制（Dual-Track Recommendation）
> 僅適用於股票/投資類調查。必須分別給出兩種建議。

### A. 新入場建議（New Entry）
| 項目 | 內容 |
|------|------|
| 建議 | [進場 / 等回調 / 不建議] |
| 建議進場區間 | [XX - YY 元] |
| 安全邊際 | [當前股價 vs Base 的差距 %] |
| 風險報酬比 | [上檔至 Bull +XX% / 下檔至 Bear -YY%] |
| 等待條件 | [若不建議立即進場，等什麼事件或價位] |

### B. 已持有建議（Current Holders）
| 項目 | 內容 |
|------|------|
| 建議 | [強力續抱 / 續抱 / 續抱觀察 / 減碼 / 停利 / 出場] |
| 停損價 | [XX 元（設定理由）] |
| 加碼觸發 | [XX 元以下 或 某事件確認] |
| 減碼觸發 | [XX 元以上 或 某風險因子轉紅] |
| 關鍵監控 | [最重要的 1-2 個觀察指標] |

> **兩個建議可以不同。** 例如：新入場不建議（超過 Base）但已持有續抱（有成本優勢+停損保護）。

---

## 🔴 退場條件（Exit Triggers）— 投資報告必填
> 僅適用於股票/投資排名類調查。若為一般OSINT調查，省略此節。

對每一檔推薦股票，必須明確說明：

| 公司 | 論點失效信號 | 停損水位 | 重新評估時間點 |
|------|------------|---------|--------------|
| [公司名] | [哪個具體事件/數據代表投資邏輯不再成立] | [股價或EPS觸發點] | [日期或事件] |

**這是強制欄位。「沒有退場條件」的推薦等同於不完整的分析。** 至少填寫以下三類：
- **催化劑失效**：若3個月催化劑未如期發生（例如出貨延後、法說會EPS miss），持有理由是否仍然成立？
- **估值破壞**：若EPS實際值低於預估值X%，P/E擴張假設是否需要重算？
- **系統性風險觸發**：若大盤或產業指數下跌超過Y%，個股護城河是否足以支撐？

## 情報缺口（Intelligence Gaps）
[未能確認的事項；後續調查建議]

## 🔴 來源審計（Source Audit）
| 類別 | 數量 | 佔比 |
|------|------|------|
| 一次來源（法規申報、官方文件、直接紀錄） | X | X% |
| 二次來源（新聞、分析報告、聚合器） | X | X% |
| **合計** | **X** | **100%** |

目標：一次來源 ≥ 40%。若低於 40%，須註明哪些發現缺乏一次來源支撐。

## 資料來源（Sources）
[所有來源附 URL，各自標註（一次來源）或（二次來源）]
```

## Confidence Framework

- **High**: Multiple independent primary sources confirm; direct evidence; internally consistent; counter-evidence search found nothing credible.
- **Medium**: Credible but not fully corroborated; strong circumstantial evidence; or single primary source not yet cross-verified.
- **Low**: Single secondary source or significant logical leaps; plausible but unverified.
- **Speculative**: Educated guess. Clearly labeled.

Always explain *why* you assigned a particular level, including what the counter-evidence search returned.
