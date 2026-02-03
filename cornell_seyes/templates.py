
from dataclasses import dataclass
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from .seyes import SeyesBlock

@dataclass(frozen=True)
class LayoutConfig:
    left_margin_pt: float = 14.17
    right_margin_pt: float = 14.17
    bottom_margin_pt: float = 14.17
    top_margin_pt: float = 18.0
    header_row_h: float = 20.0
    cornell_header_h: float = 22.0
    left_col_ratio: float = 0.36
    label_h: float = 20.0
    write_h: float = 100.0
    reflection_h: float = 60.0
    spacer_h: float = 4.0
    grid_line_w: float = 0.6
    notes_minus_pt: float = 28.35

def build_actief_leren_pdf(output_path: str, cfg: LayoutConfig = LayoutConfig()) -> str:
    page_w, page_h = A4
    usable_w = page_w - cfg.left_margin_pt - cfg.right_margin_pt
    usable_h = page_h - cfg.top_margin_pt - cfg.bottom_margin_pt

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=cfg.left_margin_pt,
        rightMargin=cfg.right_margin_pt,
        bottomMargin=cfg.bottom_margin_pt,
        topMargin=cfg.top_margin_pt,
    )

    elements = []

    header_h_total = 2 * cfg.header_row_h
    header = Table(
        [
            ["Vak:", "", "Datum:", ""],
            ["Lesonderwerp:", "", "", ""],
        ],
        colWidths=[
            95,
            0.35 * usable_w,
            60,
            usable_w - (95 + 0.35 * usable_w + 60),
        ],
        rowHeights=[cfg.header_row_h] * 2,
    )
    header.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), cfg.grid_line_w, colors.black),
        ("SPAN", (1,1), (-1,1)),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ]))
    elements.append(header)
    elements.append(Spacer(1, cfg.spacer_h))

    summary_total = 2 * (cfg.label_h) + cfg.write_h + cfg.reflection_h

    notes_h = usable_h - (
        header_h_total + cfg.spacer_h +
        cfg.cornell_header_h + cfg.spacer_h +
        summary_total
    ) + 10.0

    notes_h -= cfg.notes_minus_pt
    print(notes_h)

    left_col = cfg.left_col_ratio * usable_w
    right_col = usable_w - left_col

    left_header = Paragraph("<b>Vragen & kernbegrippen</b>", ParagraphStyle("lh", fontSize=10))
    right_header = Paragraph("<b>Lesnotities</b>", ParagraphStyle("rh", fontSize=10))

    cornell = Table(
        [
            [left_header, right_header],
            [SeyesBlock(left_col, notes_h), SeyesBlock(right_col, notes_h)],
        ],
        colWidths=[left_col, right_col],
        rowHeights=[cfg.cornell_header_h, notes_h],
    )
    cornell.setStyle(TableStyle([
        ("GRID", (0,0), (-1,0), cfg.grid_line_w, colors.black),
        ("GRID", (0,1), (-1,1), cfg.grid_line_w, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.whitesmoke),
    ]))
    elements.append(cornell)
    elements.append(Spacer(1, cfg.spacer_h))

    summary_label = Paragraph(
        "<b>Samenvatting</b> <font size=8 color=grey>(max. 5 zinnen – in eigen woorden)</font>",
        ParagraphStyle("sl", fontSize=10)
    )

    bottom = Table(
        [
            [summary_label],
            [SeyesBlock(usable_w, cfg.write_h)],
            ["Reflectie / vragen"],
            [SeyesBlock(usable_w, cfg.reflection_h)],
        ],
        colWidths=[usable_w],
        rowHeights=[cfg.label_h, cfg.write_h, cfg.label_h, cfg.reflection_h],
    )
    bottom.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), cfg.grid_line_w, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.whitesmoke),
        ("BACKGROUND", (0,2), (-1,2), colors.whitesmoke),
    ]))
    elements.append(bottom)

    back_cornell = Table(
        [
            [right_header],
            [SeyesBlock(usable_w, usable_h - cfg.cornell_header_h - 22)],
        ],
        colWidths=[usable_w],
        rowHeights=[cfg.cornell_header_h, usable_h - cfg.cornell_header_h - 22],
    )
    back_cornell.setStyle(TableStyle([
        ("GRID", (0,0), (-1,0), cfg.grid_line_w, colors.black),
        ("GRID", (0,1), (-1,1), cfg.grid_line_w, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.whitesmoke),
    ]))
    elements.append(Spacer(1, cfg.spacer_h))
    elements.append(back_cornell)

    doc.build(elements)
    return output_path
