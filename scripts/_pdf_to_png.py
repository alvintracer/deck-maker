#!/usr/bin/env python3
"""Convert PDF pages to PNG images using macOS Quartz framework."""
import Quartz
import CoreGraphics
import os

pdf_path = '/Users/milkyway/Desktop/Dev/deck-maker/materials/knpa/TranSight_Address Intelligence Report_IR-2026-0001.pdf'
output_dir = '/Users/milkyway/Desktop/Dev/deck-maker/materials/knpa/report-pages'
os.makedirs(output_dir, exist_ok=True)

# Open PDF
pdf_url = Quartz.CFURLCreateFromFileSystemRepresentation(None, pdf_path.encode('utf-8'), len(pdf_path.encode('utf-8')), False)
pdf_doc = Quartz.CGPDFDocumentCreateWithURL(pdf_url)

if pdf_doc is None:
    print("ERROR: Could not open PDF")
    exit(1)

num_pages = Quartz.CGPDFDocumentGetNumberOfPages(pdf_doc)
print(f"PDF has {num_pages} pages")

scale = 2.0  # 2x for good quality

for page_num in range(1, num_pages + 1):
    page = Quartz.CGPDFDocumentGetPage(pdf_doc, page_num)
    if page is None:
        continue
    
    page_rect = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
    width = int(page_rect.size.width * scale)
    height = int(page_rect.size.height * scale)
    
    # Create bitmap context
    cs = Quartz.CGColorSpaceCreateDeviceRGB()
    ctx = Quartz.CGBitmapContextCreate(None, width, height, 8, width * 4, cs, Quartz.kCGImageAlphaPremultipliedLast)
    
    # White background
    Quartz.CGContextSetRGBFillColor(ctx, 1.0, 1.0, 1.0, 1.0)
    Quartz.CGContextFillRect(ctx, Quartz.CGRectMake(0, 0, width, height))
    
    # Scale and draw
    Quartz.CGContextScaleCTM(ctx, scale, scale)
    Quartz.CGContextDrawPDFPage(ctx, page)
    
    # Save
    image = Quartz.CGBitmapContextCreateImage(ctx)
    output_path = os.path.join(output_dir, f'report-page-{page_num:02d}.png')
    url = Quartz.CFURLCreateFromFileSystemRepresentation(None, output_path.encode('utf-8'), len(output_path.encode('utf-8')), False)
    dest = Quartz.CGImageDestinationCreateWithURL(url, 'public.png', 1, None)
    Quartz.CGImageDestinationAddImage(dest, image, None)
    Quartz.CGImageDestinationFinalize(dest)
    
    print(f"  ✅ Page {page_num} -> {output_path}")

print(f"\n🎯 Done! {num_pages} pages converted.")
