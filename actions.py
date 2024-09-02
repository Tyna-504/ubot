from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

    
class ValidateSessionTypeAction(Action):
    def name(self) -> Text:
        return "action_validate_session_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        session_type = tracker.get_slot("session_type")

        valid_session_types = ["academic", "career", "well-being"]

        if session_type not in valid_session_types:
            dispatcher.utter_message(text="Sorry, that's not a valid session type. Please choose from 'academic', 'career', or 'well-being'.")
            return [SlotSet("session_type", None)]

        return []
