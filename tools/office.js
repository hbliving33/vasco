// Builds the Vasco Solar Word letterhead and PowerPoint template into assets/brand/kit/.
// Run from the repo root:  node tools/office.js
const fs = require("fs");
const path = require("path");
const docx = require("docx");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const KIT = path.join(__dirname, "..", "assets", "brand", "kit");
const img = (f) => fs.readFileSync(path.join(KIT, f));
const ADDR = "17150 Newhope St #403, Fountain Valley, CA 92708";
const PHONE = "(714) 968-8845";
const LIC = "CSL# 608260";

// ------------------------------------------------------------------ Word letterhead
async function letterhead() {
  const { Document, Packer, Paragraph, TextRun, ImageRun, Header, Footer, AlignmentType, BorderStyle, TabStopType } = docx;
  const p = (text, opts = {}) => new Paragraph({ spacing: { after: 160 }, ...opts, children: [new TextRun({ text, ...(opts.run || {}) })] });
  const doc = new Document({
    creator: "Vasco Solar", title: "Vasco Solar Letterhead",
    styles: {
      default: { document: { run: { font: "Arial", size: 21, color: "1B2430" } } },
      paragraphStyles: [
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { font: "Arial", size: 28, bold: true, color: "1850A0" }, paragraph: { spacing: { before: 240, after: 120 }, keepNext: true, outlineLevel: 0 } },
      ],
    },
    sections: [{
      properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 2160, bottom: 1440, left: 1440, right: 1440, header: 600, footer: 500 } } },
      headers: { default: new Header({ children: [
        new Paragraph({
          tabStops: [{ type: TabStopType.RIGHT, position: 9360 }],
          border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: "86D2EC", space: 8 } },
          children: [
            new ImageRun({ type: "png", data: img("logo-color.png"), transformation: { width: 190, height: 96 }, altText: { title: "Vasco Solar Energy", description: "Vasco Solar Energy logo", name: "logo" } }),
            new TextRun({ text: "\tSolar power solutions since 1989", color: "1850A0", bold: true, size: 18 }),
          ] }),
      ] }) },
      footers: { default: new Footer({ children: [
        new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 6, color: "86D2EC", space: 6 } },
          children: [new TextRun({ text: `${ADDR}  ·  ${PHONE}  ·  ${LIC}`, size: 16, color: "5B6878" })] }),
      ] }) },
      children: [
        p("[Date]", { spacing: { before: 240, after: 160 } }),
        p("[Recipient Name]", { spacing: { after: 0 } }), p("[Street Address]", { spacing: { after: 0 } }), p("[City, State ZIP]", { spacing: { after: 320 } }),
        p("Dear [Recipient Name],"),
        p("Type your letter here.  This letterhead uses Arial, the Vasco brand blue for headings, and the logo and contact details in the header and footer, so every letter matches."),
        p("To start a new letter, open this file, replace the bracketed text, and save it under a new name."),
        p("Sincerely,", { spacing: { before: 240, after: 720 } }),
        p("[Your Name]", { spacing: { after: 0 } }), p("[Title]", { spacing: { after: 0 } }), p("Vasco Solar"),
      ],
    }],
  });
  fs.writeFileSync(path.join(KIT, "vasco-letterhead.docx"), await Packer.toBuffer(doc));
}

// ------------------------------------------------------------------ PowerPoint template
async function deck() {
  const THEME = { name: "Vasco Solar", headFontFace: "Arial", bodyFontFace: "Calibri",
    colors: { dk1: "1B2430", lt1: "FFFFFF", dk2: "0E2740", lt2: "F5F7FA", accent1: "1850A0", accent2: "F4C21C", accent3: "86D2EC",
              accent4: "F2E600", accent5: "5B6878", accent6: "2E7D4F", hlink: "1850A0", folHlink: "0E2740" } };
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.author = "Vasco Solar"; pres.company = "Vasco Solar"; pres.title = "Vasco Solar Presentation Template";
  const C = pres.SchemeColor;
  const logoRev = "data:image/png;base64," + img("logo-reverse.png").toString("base64");
  const logoCol = "data:image/png;base64," + img("logo-color.png").toString("base64");
  const iconRev = "data:image/png;base64," + img("icon-reverse.png").toString("base64");
  const footer = { text: `Vasco Solar  ·  ${PHONE}  ·  ${LIC}`, options: { x: 0.6, y: 6.95, w: 8, h: 0.3, fontSize: 10, color: C.accent5 } };

  pres.defineSlideMaster({ title: "TITLE", background: { color: C.text2 },
    objects: [{ image: { data: logoRev, x: 0.6, y: 0.55, w: 3.4, h: 1.72 } },
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 3.0, w: 11.5, h: 1.4, fontSize: 44, bold: true, color: C.background1, valign: "bottom", align: "left", margin: 0 }, text: "Presentation title" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 4.55, w: 11.5, h: 0.9, fontSize: 20, color: C.accent3, margin: 0 }, text: "Subtitle or date" } },
      { text: { text: `${PHONE}  ·  ${LIC}`, options: { x: 0.6, y: 6.7, w: 8, h: 0.35, fontSize: 12, color: C.accent2, margin: 0 } } }] });
  pres.defineSlideMaster({ title: "SECTION", background: { color: C.accent1 },
    objects: [{ image: { data: iconRev, x: 9.1, y: 1.85, w: 3.6, h: 3.6 } },
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 2.6, w: 8.2, h: 1.3, fontSize: 40, bold: true, color: C.background1, align: "left", valign: "bottom", margin: 0 }, text: "Section title" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 3.95, w: 8.2, h: 0.8, fontSize: 18, color: C.background1, margin: 0 }, text: "One line about this section" } }] });
  pres.defineSlideMaster({ title: "CONTENT", background: { color: C.background1 }, slideNumber: { x: 12.3, y: 6.95, w: 0.5, h: 0.3, fontSize: 10, color: C.accent5 },
    objects: [{ image: { data: logoCol, x: 11.2, y: 0.35, w: 1.6, h: 0.81 } }, { text: footer },
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.45, w: 10.3, h: 0.9, fontSize: 32, bold: true, color: C.text2, align: "left", valign: "middle", margin: 0 }, text: "Slide title" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 1.65, w: 12.1, h: 5.0, fontSize: 18, color: C.text1, margin: 0 }, text: "Body text" } }] });
  pres.defineSlideMaster({ title: "TITLE_ONLY", background: { color: C.background1 }, slideNumber: { x: 12.3, y: 6.95, w: 0.5, h: 0.3, fontSize: 10, color: C.accent5 },
    objects: [{ image: { data: logoCol, x: 11.2, y: 0.35, w: 1.6, h: 0.81 } }, { text: footer },
      { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 0.45, w: 10.3, h: 0.9, fontSize: 32, bold: true, color: C.text2, align: "left", valign: "middle", margin: 0 }, text: "Slide title" } }] });
  pres.defineSlideMaster({ title: "CLOSING", background: { color: C.text2 },
    objects: [{ image: { data: logoRev, x: 4.37, y: 1.2, w: 4.6, h: 2.32 } },
      { placeholder: { options: { name: "title", type: "title", x: 1, y: 4.0, w: 11.33, h: 0.9, fontSize: 36, bold: true, color: C.background1, align: "center", margin: 0 }, text: "Thank you" } },
      { text: { text: `${PHONE}  ·  ${ADDR}  ·  ${LIC}`, options: { x: 1, y: 5.1, w: 11.33, h: 0.4, fontSize: 14, color: C.accent2, align: "center", margin: 0 } } }] });

  pres.addSection({ title: "Opening" });
  let s = pres.addSlide({ masterName: "TITLE", sectionTitle: "Opening" });
  s.addText("Going solar with Vasco", { placeholder: "title" }); s.addText("Presentation template", { placeholder: "body" });

  pres.addSection({ title: "Content" });
  s = pres.addSlide({ masterName: "SECTION", sectionTitle: "Content" });
  s.addText("Why Vasco Solar", { placeholder: "title" }); s.addText("Use this layout to start each part of your talk", { placeholder: "body" });

  s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Content" });
  s.addText("Slide title goes here", { placeholder: "title" });
  s.addText([
    { text: "Custom-designed systems sized to your roof, usage and budget", options: { bullet: true, breakLine: true } },
    { text: "$0-down financing with no prepayment penalty", options: { bullet: true, breakLine: true } },
    { text: "Monitoring from your phone or computer", options: { bullet: true, breakLine: true } },
    { text: "Licensed California solar contractor since 1989", options: { bullet: true } },
  ], { placeholder: "body", paraSpaceAfter: 10 });

  s = pres.addSlide({ masterName: "TITLE_ONLY", sectionTitle: "Content" });
  s.addText("Numbers that matter", { placeholder: "title" });
  [["1989", "Serving Southern California since"], ["Top 500", "Solar Power World contractor list"], ["$0 down", "Financing available"]].forEach(([n, l], i) => {
    const x = 0.6 + i * 4.1;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 2.0, w: 3.8, h: 3.4, fill: { color: C.background2 }, line: { color: C.background2 }, objectName: `stat-${i + 1}` });
    s.addText(n, { x: x + 0.3, y: 2.5, w: 3.2, h: 1.3, fontSize: 54, bold: true, color: C.accent1, fontFace: "Arial", margin: 0, isTextBox: true });
    s.addText(l, { x: x + 0.3, y: 3.9, w: 3.2, h: 1.0, fontSize: 16, color: C.text1, margin: 0, valign: "top", isTextBox: true });
  });

  s = pres.addSlide({ masterName: "TITLE_ONLY", sectionTitle: "Content" });
  s.addText("Two-column comparison", { placeholder: "title" });
  [["Solar electricity", ["Lower monthly electric bills", "Protection from rate increases", "Higher home value"]],
   ["Battery storage", ["Backup power during outages", "Use your solar after sunset", "Covers the 4 to 9 p.m. peak"]]].forEach(([h, items], i) => {
    const x = 0.6 + i * 6.2;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 1.75, w: 5.9, h: 4.8, fill: { color: C.background2 }, line: { color: C.background2 }, objectName: `column-${i + 1}` });
    s.addText(h, { x: x + 0.4, y: 2.05, w: 5.1, h: 0.6, fontSize: 24, bold: true, color: C.accent1, fontFace: "Arial", margin: 0, isTextBox: true });
    s.addText(items.map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < items.length - 1 } })),
      { x: x + 0.4, y: 2.85, w: 5.1, h: 3.3, fontSize: 18, color: C.text1, margin: 0, valign: "top", paraSpaceAfter: 10, isTextBox: true });
  });

  pres.addSection({ title: "Closing" });
  s = pres.addSlide({ masterName: "CLOSING", sectionTitle: "Closing" });
  s.addText("Thank you", { placeholder: "title" });

  const out = path.join(KIT, "vasco-presentation.pptx");
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
}

(async () => { await letterhead(); await deck(); console.log("office files built"); })();
