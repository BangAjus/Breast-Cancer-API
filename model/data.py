from pydantic import BaseModel, Field

class Features(BaseModel):

    clump_thickness: float = Field(..., ge=1, le=10)
    uniformity_of_cell_size: float = Field(..., ge=1, le=10)
    uniformity_of_cell_shape: float = Field(..., ge=1, le=10)
    marginal_adhesion: float = Field(..., ge=1, le=10)
    single_epithelial_cell_size: float = Field(..., ge=1, le=10)
    bare_nuclei: float = Field(..., ge=1, le=10)
    bland_chromatin: float = Field(..., ge=1, le=10)
    normal_nucleoli: float = Field(..., ge=1, le=10)
    mitoses: float = Field(..., ge=1, le=10)