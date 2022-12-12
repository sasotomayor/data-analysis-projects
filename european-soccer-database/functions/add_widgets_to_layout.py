
def add_wigets_to_layout(layout, widgets, widget = True):
    if widget:
        for widget in widgets:
            layout.addWidget(widget)
    else:
        for sub_layout in widgets:
            layout.addLayout(sub_layout)
    return layout
        