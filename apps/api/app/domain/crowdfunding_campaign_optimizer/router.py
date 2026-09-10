from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.crowdfunding_campaign_optimizer.schemas import AgenticCrowdfundingCampaignOptimizerSessionCreate, AgenticCrowdfundingCampaignOptimizerSessionResponse
from app.domain.crowdfunding_campaign_optimizer.service import AgenticCrowdfundingCampaignOptimizerService

router = APIRouter(prefix="/api/v1/crowdfunding_campaign_optimizer", tags=["Agentic Crowdfunding Campaign Optimizer Domain"])

@router.post("/sessions", response_model=AgenticCrowdfundingCampaignOptimizerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticCrowdfundingCampaignOptimizerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Crowdfunding Campaign Optimizer.
    """
    return AgenticCrowdfundingCampaignOptimizerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticCrowdfundingCampaignOptimizerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticCrowdfundingCampaignOptimizerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
