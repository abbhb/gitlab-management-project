class DjangoConfig():
    """
    Django 配置
    """

    use_tz: bool = Field(default=True, alias="USE_TZ", description="是否使用时区")
    databases: dict[str, Database] = Field(default_factory=lambda: {"default": Database()}, alias="DATABASES")
    installed_apps: list[str] = Field(default_factory=lambda: _INSTALLED_APPS, alias="INSTALLED_APPS")
    default_auto_field: str = Field(default="django.db.models.BigAutoField", alias="DEFAULT_AUTO_FIELD")

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(populate_by_name=True)