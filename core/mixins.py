class AdminDisplayNameMixin:
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ('id',)


class AdminDisplayTitleMixin:
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    ordering = ('id',)