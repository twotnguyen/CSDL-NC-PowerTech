#!/usr/bin/env python3
"""Chạy toàn bộ quy trình sinh báo cáo theo đúng thứ tự: sơ đồ ERD, SQL tạo bảng, các chương, rồi ghép .docx.
Chạy:  python3 tools/chay_het.py   (từ thư mục bao-cao-moi)"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
for script in ('ve_erd3.py', 've_bang.py', 've_so_do_tong.py', 've_usecase.py', 've_luudo.py', 'sql_gen.py', 'gen_chuong1.py', 'gen_chuong2.py', 'gen_chuong3.py', 'gen_chuong4.py', 'ghep_docx.py'):
    print('==', script)
    subprocess.run([sys.executable, os.path.join(HERE, script)], check=True)
