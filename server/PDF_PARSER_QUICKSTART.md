# 🚀 PDF Parser PoC - Quick Start Guide

## Phase 0 Validation Sprint (Jan 13-19, 2025)

**Goal:** Test PDF parsing accuracy on real M-Pesa PDFs → Target: 85-90%+

---

## Step 1: Setup (5 minutes)

```bash
# Navigate to server directory
cd /home/mo/dev/mpesa-recon/server

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install tabulate  # For nice table output

# Create test directory
mkdir -p test_pdfs
```

---

## Step 2: Add Your PDFs (You're doing this now!)

Place your M-Pesa PDFs in `server/test_pdfs/`:

```bash
server/
  test_pdfs/
    esther_1page.pdf          # 1-page sample
    kenneth_3page.pdf         # 3-page sample
    david_8page_2025.pdf      # 8-page 2025 sample
    # Add more PDFs here (target: 20 total)
```

**PDF Sources:**
- ✅ Scribd (you mentioned downloading)
- Grace's network (redacted samples)
- Upwork: "Kenyan M-Pesa PDF redaction" ($20 for 5-10 samples)

---

## Step 3: Run Test Script (30 seconds)

```bash
# Make script executable
chmod +x test_pdf_parser.py

# Run tests
python test_pdf_parser.py
```

**Interactive prompts:**
1. "Are any PDFs password-protected?" → Enter `y` or `n`
2. If yes: "Enter password (usually your ID number)" → Enter ID

---

## Step 4: Review Results

The script will output:

### Per-File Results:
```
Testing: esther_1page.pdf
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 File: esther_1page.pdf
📏 Size: 125.34 KB
📑 Pages: 1
🔍 Parsing Method: table
📝 Statement Type: M-PESA STATEMENT

✅ Transactions Found: 23
🔑 Unique Transaction IDs: 23

📊 Sample Transactions (first 5):
┌────────────┬────────────────┬──────────┬─────────────────────────────────────────┐
│ Date       │ Transaction ID │ Amount   │ Description                             │
├────────────┼────────────────┼──────────┼─────────────────────────────────────────┤
│ 2024-12-15 │ RKG7N5QWXT...  │ 2500.00  │ Paid to John Doe                        │
│ 2024-12-16 │ QCV7LT9CDB...  │ 1200.00  │ Received from Jane Smith                │
└────────────┴────────────────┴──────────┴─────────────────────────────────────────┘

🎯 Estimated Accuracy: 92.5%
```

### Summary:
```
📊 SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌─────────────────────┬────────┬──────────────┬──────────┬───────┐
│ File                │ Status │ Transactions │ Accuracy │ Pages │
├─────────────────────┼────────┼──────────────┼──────────┼───────┤
│ esther_1page.pdf    │ ✅     │ 23           │ 92.5%    │ 1     │
│ kenneth_3page.pdf   │ ✅     │ 67           │ 88.3%    │ 3     │
│ david_8page.pdf     │ ✅     │ 189          │ 91.7%    │ 8     │
└─────────────────────┴────────┴──────────────┴──────────┴───────┘

✅ Successfully Parsed: 3/3 files
📈 Total Transactions: 279
🎯 Average Accuracy: 90.8%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧭 DECISION GUIDANCE (for Jan 27 GO/NO-GO):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ STRONG GO: 90.8% accuracy exceeds 90% target!
   → Parser is ready for MVP build
```

---

## Step 5: Manual Validation (CRITICAL!)

**Don't trust the automated accuracy estimate alone!**

### Manual Check (10 minutes per PDF):
1. Open PDF in browser/viewer
2. Pick 10 random transactions
3. Compare PDF vs script output:
   - ✅ Transaction ID matches?
   - ✅ Date correct?
   - ✅ Amount correct?
   - ✅ Description captured?

### Calculate Real Accuracy:
```
Real Accuracy = (Correct Transactions / 10) × 100%

Example: 9/10 correct = 90% accuracy
```

---

## Step 6: Document Edge Cases

While testing, note any issues:

```markdown
## Edge Cases Found:

1. **Date Format Issue** (kenneth_3page.pdf)
   - PDF has: "15/12/24"
   - Parser got: null
   - Fix: Add format "%d/%m/%y"

2. **Special Characters** (david_8page.pdf)
   - PDF has: "Paid to CAFÉ MOCHA"
   - Parser got: "Paid to CAF MOCHA" (accent lost)
   - Fix: UTF-8 encoding

3. **Split Transactions** (esther_1page.pdf)
   - Transaction spans 2 rows in table
   - Parser extracted 2 separate transactions
   - Fix: Row merging logic
```

---

## Decision Gates (Jan 27)

### ✅ STRONG GO (>90% accuracy)
→ Parser ready for MVP  
→ Start Phase 1 build (Feb 1)

### ✅ GO (85-90% accuracy)
→ Parser usable with improvements  
→ Continue to Phase 1, iterate during build

### ⚠️  YELLOW (70-85% accuracy)
→ Hybrid approach needed:
- Auto-parse first
- Manual review UI for flagged transactions
- User confirms/edits before report generation

### ❌ RED (<70% accuracy)
→ Major issue, consider:
- More parser development (add 2 weeks)
- API-first approach (Daraja, but excludes informal sector)
- Pivot to different data source

---

## Next Steps After Testing

### If Accuracy ≥ 85%:
1. ✅ Test 17 more PDFs (total 20)
2. Document common patterns
3. Update parser for edge cases
4. Ready for Phase 1!

### If Accuracy < 85%:
1. Analyze failure patterns
2. Improve parser logic (2-3 days)
3. Re-test with same PDFs
4. If still low: Consider hybrid approach

---

## Troubleshooting

### "Import Error: pdfplumber not found"
```bash
pip install -r requirements.txt
```

### "Password Error" for encrypted PDFs
M-Pesa PDFs use your **ID number** as password (not phone number!)

### "No transactions found"
- Check if PDF is correct format (not scanned image)
- Try different PDFs
- Check parser logs for errors

### Script crashes
```bash
# Check Python version (need 3.11+)
python --version

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

---

## Files Created

```
server/
  ├── app/services/pdf_service.py     # ✅ Updated with password support
  ├── requirements.txt                # ✅ Added pikepdf
  ├── test_pdf_parser.py              # ✅ NEW: Test script
  └── test_pdfs/                      # 📁 Your PDFs go here
      ├── esther_1page.pdf
      ├── kenneth_3page.pdf
      └── david_8page_2025.pdf
```

---

## Quick Command Reference

```bash
# Setup
cd server && source venv/bin/activate
pip install -r requirements.txt tabulate

# Run tests
python test_pdf_parser.py

# Check specific PDF manually
python -c "
from app.services.pdf_service import pdf_parser
txns, meta = pdf_parser.parse_pdf('test_pdfs/your_file.pdf', password='12345678')
print(f'Found {len(txns)} transactions')
"
```

---

**🎯 Your Target:** 85-90%+ accuracy on 20 PDFs by Jan 27

**⏱️  Time Budget:** 
- Setup: 5 min
- Testing 3 PDFs: 10 min
- Manual validation: 30 min
- **Total: 45 minutes** → You'll know if parser works!

Good luck! 🚀
