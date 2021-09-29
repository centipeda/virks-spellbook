
from PIL import Image, ImageDraw, ImageFont, ImageColor
import os

CARD_W = 750
CARD_H = 1050

TITLE_FONT_SIZE    = 55
SUBTITLE_FONT_SIZE = 36
BODY_FONT_SIZE     = 24

BLACK    = (0,0,0)
DARK_RED = ImageColor.getrgb("#58180D")

def getpath(path):
    return os.path.join(os.path.dirname(__file__), path)

title_font = ImageFont.truetype(getpath("Modesto Condensed Bold.ttf"), size=TITLE_FONT_SIZE)
subtitle_font = ImageFont.truetype(getpath("mrs-eaves-small-caps.ttf"), size=SUBTITLE_FONT_SIZE)
body_font = ImageFont.truetype(getpath("ScalaSans-RegularLF.otf"), size=BODY_FONT_SIZE)
body_font_bold = ImageFont.truetype(getpath("ScalaSans-BoldLF.otf"), size=BODY_FONT_SIZE)

def split_line(font, lines, margin, indent=0):
    text = []
    break_point = CARD_W - margin
    for line in lines:
        # start at beginning of line
        curr_line = line
        length = 0
        index = -1
        while True:
            # find the next word to break at
            new_index = curr_line.find(" ", index+1)
            if new_index < 0:
                text.append(curr_line.strip())
                break
            # get the point where the line will end given the new index
            length = indent + font.getlength(curr_line[:new_index])
            # check if we're past the linebreak point
            if length+margin >= break_point:
                # if we are, append the text we have now
                text.append(curr_line[:index].strip())
                # chop off the line we just measured
                curr_line = curr_line[index:]
                # reset the index and indent
                index = 0
                indent = 0
                continue
            index = new_index
        indent = 0
        text.append("")
    return text

def draw_border(draw):
    border_width = 20
    border_padding = 5
    border_color = BLACK
    draw.line((0, 0, 0, CARD_H), width=border_width*2, fill=border_color)
    draw.line((CARD_W, 0, CARD_W, CARD_H), width=border_width*2, fill=border_color)
    draw.line((0, 0, CARD_W, 0), width=border_width*2, fill=border_color)
    draw.line((0, CARD_H, CARD_W, CARD_H), width=border_width*2, fill=border_color)

    draw.line((0, 0, 0, CARD_H), width=border_padding*2, fill=(255, 255, 255))
    draw.line((CARD_W, 0, CARD_W, CARD_H), width=border_padding*2, fill=(255, 255, 255))
    draw.line((0, 0, CARD_W, 0), width=border_padding*2, fill=(255, 255, 255))
    draw.line((0, CARD_H, CARD_W, CARD_H), width=border_padding*2, fill=(255, 255, 255))
    return draw

def draw_title(draw, text):
    title_offset = (CARD_W - title_font.getlength(text)) / 2
    draw.text((title_offset, 25), text, font=title_font, fill=DARK_RED)
    return draw

def draw_subtitle(draw, text):
    level_offset = (CARD_W - subtitle_font.getlength(text)) / 2
    draw.text((level_offset, 100), text, font=subtitle_font, fill=(0,0,0))
    return draw

def draw_desc_at(draw, lines, xy, offset):
    x,y = xy
    for line in lines:
        draw.text((x, y), line, font=body_font, fill=(0,0,0))
        y += offset
    return draw

def gen_cards(spell):
    # set up objects
    img = Image.new(mode="RGB", size=(CARD_W, CARD_H), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # draw border
    draw = draw_border(draw)

    # draw title
    draw = draw_title(draw, spell["title"])
    # draw spell level
    draw = draw_subtitle(draw, spell["type"])

    _l = 75
    _w = body_font_bold.getlength("Casting Time: ")
    _h = 150
    draw.text((_l, _h), "Casting Time: ", font=body_font_bold, fill=(0,0,0))
    draw.text((_l+_w, _h), spell['cast_time'], font=body_font, fill=(0,0,0))

    _w = body_font_bold.getlength("Range: ")
    _h = 180
    draw.text((_l, _h), "Range: ", font=body_font_bold, fill=(0,0,0))
    draw.text((_l+_w, _h), spell['range'], font=body_font, fill=(0,0,0))

    _w = body_font_bold.getlength("Duration: ")
    _h = 210
    draw.text((_l, _h), "Duration: ", font=body_font_bold, fill=(0,0,0))
    draw.text((_l+_w, _h), spell['duration'], font=body_font, fill=(0,0,0))

    _w = body_font_bold.getlength("Components: ")
    _h = 240
    draw.text((_l, _h), "Components: ", font=body_font_bold, fill=(0,0,0))
    comp_lines = split_line(body_font, [spell['components']], 75, indent=_w)
    draw.text((_l+_w, _h), comp_lines[0], font=body_font, fill=(0,0,0))
    if len(comp_lines) > 1:
        for line in comp_lines[1:]:
            _h += 30
            draw.text((_l, _h), line, font=body_font, fill=(0,0,0))

    _h += 30
    lines = split_line(body_font, spell['description'], 75)
    break_line = 0
    for i in range(len(lines)):
        break_line = i
        if _h + 27*i > CARD_H-50:
            break
    
    # draw our description
    draw = draw_desc_at(draw, lines[:break_line], (_l, _h), 27)
    
    imgs = [img]

    # generate additional card(s)
    _h = 150+35
    while break_line < len(lines)-1:
        lines = lines[break_line:]
        for i in range(len(lines)):
            break_line = i
            if _h + 27*i > CARD_H - 50:
                break
        _i = Image.new(mode="RGB", size=(CARD_W, CARD_H), color=(255, 255, 255))
        _d = ImageDraw.Draw(_i)
        _d = draw_border(_d)
        _d = draw_title(_d, spell["title"])
        _d = draw_subtitle(_d, spell["type"])
        offset = (CARD_W - body_font.getlength("(cont'd)"))/2
        _d.text((offset, 150), "(cont'd)", font=body_font, fill=(0,0,0))
        _d = draw_desc_at(_d, lines[:break_line], (_l, _h), 27)
        imgs.append(_i)
    return imgs

def make_printable(cards, file):
    pages = []
    position = 1
    _p = Image.new(mode="RGB", size=(2250, 3000), color=(255, 255, 255))
    while cards:
        if position > 3:
            x = 75
            _pos = position - 3
        else:
            x = 75 + CARD_H
            _pos = position
        y = 300 + CARD_W*(_pos-1)

        card = cards.pop(0)
        card = card.transpose(Image.ROTATE_270)
        _p.paste(card, (x, y))

        position += 1
        if position > 6:
            pages.append(_p)
            _p = Image.new(mode="RGB", size=(2250, 3000), color=(255, 255, 255))
            position = 1
    if position != 1:
        pages.append(_p)
    p = pages.pop(0)
    p.save(file, format="PDF", save_all=True, title="Spell Cards", append_images=pages)
