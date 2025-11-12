#!/bin/bash
# Quick PDF Parser Test Runner

echo "🚀 M-Recon PDF Parser Test"
echo "=========================="
echo ""

# Check if we're in the server directory
if [ ! -f "test_pdf_parser.py" ]; then
    echo "❌ Error: Must run from server/ directory"
    echo "   cd /home/mo/dev/mpesa-recon/server"
    exit 1
fi

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "❌ Error: Virtual environment not found"
    echo "   Create it first: python3 -m venv venv"
    exit 1
fi

# Activate venv
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if dependencies installed
echo "🔍 Checking dependencies..."
python -c "import pdfplumber, pikepdf, pandas, tabulate" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📥 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check for test PDFs
pdf_count=$(ls test_pdfs/*.pdf 2>/dev/null | wc -l)
if [ $pdf_count -eq 0 ]; then
    echo "❌ No PDF files found in test_pdfs/"
    echo ""
    echo "📁 Please add your M-Pesa PDFs to:"
    echo "   $(pwd)/test_pdfs/"
    echo ""
    echo "📄 Supported formats:"
    echo "   - Personal M-Pesa Statement"
    echo "   - Business M-Pesa Statement"
    echo "   - Pochi la Biashara Statement"
    exit 1
fi

echo "✅ Found $pdf_count PDF file(s)"
echo ""

# Run tests
echo "🧪 Running parser tests..."
echo ""
python test_pdf_parser.py

# Deactivate venv
deactivate

echo ""
echo "✅ Test complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Review accuracy results above"
echo "   2. Manually validate sample transactions"
echo "   3. Test with more PDFs (target: 20 total)"
echo "   4. Document edge cases"
echo ""
echo "🎯 Target: 85-90%+ accuracy for GO decision (Jan 27)"
