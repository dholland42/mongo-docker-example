from pydantic import BaseModel, ConfigDict, alias_generators


APIObjectConfig = ConfigDict(alias_generator=alias_generators.to_pascal)



class FullStudySection(BaseModel):
    srg_code: str | None
    name: str | None
    srg_flex: str | None
    sra_designator_code: str | None
    sra_flex_code: str | None
    group_code: str | None

    model_config = APIObjectConfig


class DataRow(BaseModel):
    fiscal_year: int | None
    award_amount: int | None
    full_study_section: FullStudySection

    model_config = APIObjectConfig


class RequestPayload(BaseModel):
    criteria: dict = dict()
    include_fields: list[str | None] = [f.alias for f in DataRow.model_fields.values()]
    offset: int = 0
    limit: int = 25
    sort_field: str = "project_start_date"
    sort_order: str = "desc"

