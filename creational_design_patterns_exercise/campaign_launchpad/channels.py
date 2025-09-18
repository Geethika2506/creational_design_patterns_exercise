
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        pass

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
  def __init__(self):
      super().__init__("Google Ads")
      
  def create_campaign(self, campaign: Campaign) -> str:
    GlobalBudget.get_instance().allocate(campaign.daily_budget)
    return f"g-{uuid4()}"

  def pause_campaign(self, campaign_id:str) ->None:
    pass

class FacebookAdsClient(ChannelClient):
  def __init__(self):
      super().__init__("Facebook Ads")
  
  def create_campaign(self,campaign:Campaign) -> str:
    GlobalBudget.get_instance().allocate(campaign.daily_budget)
    return f"f-{uuid4()}"

  def pause_campaign(self, campaign_id:str) -> None:
    pass 

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
        channel = channel.lower()
        if channel =="google":
            return GoogleAdsClient()
        elif channel =="facebook":
           return FacebookAdsClient()
        else:
            raise ValueError(f"Unknown channel: {channel}")
        
