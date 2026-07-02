import matplotlib as mpl

def set_publication_style():
    mpl.rcParams.update({
        'font.size': 9, # journals typically want 7-9pt at final print size
        'font.family': 'sans-serif',
'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'], # Arial is the most common 'axes.titlesize': 10,
'axes.labelsize': 9,
'xtick.labelsize': 8,
'ytick.labelsize': 8,
'legend.fontsize': 8,
'axes.linewidth': 0.8,
'xtick.major.width': 0.8,
'ytick.major.width': 0.8,
'axes.spines.top': False, # remove the box's top border — cleaner, standard journal 'axes.spines.right': False, # remove right border
'figure.dpi': 150, # for on-screen preview while working
'savefig.dpi': 300, # 300 DPI minimum — the standard journal requirement 'savefig.bbox': 'tight', # trims excess whitespace automatically
'pdf.fonttype': 42, # CRITICAL: embeds fonts as editable text in PDF (not 'ps.fonttype': 42, # so journals/Illustrator can edit text later — required
})