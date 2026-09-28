from fastapi import FastAPI  # type: ignore[import-not-found]
from services.patient_service import PatientService  # type: ignore[import-not-found]
from infrastructure.memory_patient_repo import InMemoryPatientRepository  # type: ignore[import-not-found]
from domain.ews_calculator import EarlyWarningScoreCalculator  # type: ignore[import-not-found]

app = FastAPI()

repo = InMemoryPatientRepository()
calculator = EarlyWarningScoreCalculator()
service = PatientService(repo, calculator)

@app.get("/patients/{patient_id}/risk-score")
def risk_score(patient_id: str):
    return {"risk_score": service.get_risk_score(patient_id)}
