import re

def fix_css_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    style_start = content.find('<style>')
    style_end = content.find('</style>', style_start)
    if style_start == -1 or style_end == -1:
        return
    
    style2_start = content.find('<style>', style_end)
    style2_end = content.find('</style>', style2_start)
    
    lines = content.split('\n')
    
    new_lines = []
    
    # We will just parse each block of CSS and fix it.
    # To be safe, let's fix known bad lines by regex.
    # Any line starting with "body > section.page:nth-of-type(" and ending with ","
    # where the block's final selector has a suffix.
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("body > section.page:nth-of-type(") and line.endswith(","):
            # collect block of selectors
            start_i = i
            selectors = []
            while lines[i].startswith("body > section.page:nth-of-type(") and lines[i].endswith(","):
                selectors.append(lines[i])
                i += 1
            
            if lines[i].startswith("body > section.page:nth-of-type(") and "{" in lines[i]:
                last_selector = lines[i].split("{")[0].strip()
                # find the suffix
                # e.g. "body > section.page:nth-of-type(198) .table-summary li"
                m = re.match(r"(body > section\.page:nth-of-type\(\d+\))(.*)", last_selector)
                if m:
                    suffix = m.group(2)
                    if suffix: # If there's a suffix like " .bullet-list li"
                        # Apply to all collected selectors
                        for j in range(len(selectors)):
                            # Remove the comma, add suffix, add comma back
                            sel_base = selectors[j].strip()[:-1]
                            # wait, what if it already has the suffix?
                            if not sel_base.endswith(suffix.strip()):
                                # If it's something like `body > section... .data-table`, but the suffix is `.data-table.ultra`, it might be tricky.
                                # Let's do a simpler replace: extract base `body > section.page:nth-of-type(\d+)`
                                m2 = re.match(r"(body > section\.page:nth-of-type\(\d+\))(.*)", sel_base)
                                if m2 and not m2.group(2):
                                    new_lines.append(m2.group(1) + suffix + ",")
                                else:
                                    # For lines 476-542, we have:
                                    # body > section.page:nth-of-type(4) .data-table,
                                    # but we want it to be .data-table.ultra or .data-table.dense
                                    # If the block has a specific suffix and the current doesn't match
                                    if m2 and m2.group(2).strip() == ".data-table":
                                        if ".data-table.ultra" in suffix or ".data-table.dense" in suffix:
                                            new_lines.append(m2.group(1) + suffix + ",")
                                        else:
                                            new_lines.append(selectors[j])
                                    else:
                                        new_lines.append(selectors[j])
                            else:
                                new_lines.append(selectors[j])
                        new_lines.append(lines[i])
                    else:
                        for s in selectors: new_lines.append(s)
                        new_lines.append(lines[i])
                else:
                    for s in selectors: new_lines.append(s)
                    new_lines.append(lines[i])
            else:
                for s in selectors: new_lines.append(s)
                new_lines.append(lines[i]) # this might be something else
        else:
            new_lines.append(line)
        i += 1
        
    with open("fixed.html", "w") as f:
        f.write('\n'.join(new_lines))

fix_css_file('/Users/milkyway/Desktop/Dev/deck-maker/decks/ewha_thesis_presentation_deck_v11.html')
