from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.crowdfunding_campaign_optimizer.models import AgenticCrowdfundingCampaignOptimizerSession, AgenticCrowdfundingCampaignOptimizerItem
from app.domain.crowdfunding_campaign_optimizer.schemas import AgenticCrowdfundingCampaignOptimizerSessionCreate, AgenticCrowdfundingCampaignOptimizerItemCreate

class AgenticCrowdfundingCampaignOptimizerService:
    @staticmethod
    def create_session(db: Session, data: AgenticCrowdfundingCampaignOptimizerSessionCreate) -> AgenticCrowdfundingCampaignOptimizerSession:
        db_obj = AgenticCrowdfundingCampaignOptimizerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticCrowdfundingCampaignOptimizerSession:
        return db.query(AgenticCrowdfundingCampaignOptimizerSession).filter(AgenticCrowdfundingCampaignOptimizerSession.id == session_id).first()
