import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def __parse_token(token_path="token.json", token_key="bot-token"):
    """Given a json path returns the value associated to the `token_key`"""
    with open(token_path) as f:
        data = json.load(f)
    return data[token_key]


def __create_slack(slack_api_token):
    """ Create a slack client"""
    slack = WebClient(token=slack_api_token) 
    return slack    

def __send_message(slack, message, channel, username, emoji):
    """Wrapper for sending a message to a channel (or a person)"""
    try:
        result = slack.chat_postMessage(
            channel=channel,
            text=message,
            username=username,
            icon_emoji=emoji,
        )
        return result

    except SlackApiError as e:
        print(f"Error: {e}")
    return {}

    
def msg(message, channel="general", username="Thibaud", emoji=":face_with_cowboy_hat:"):
    token = __parse_token()
    slack = __create_slack(token)
    __send_message(
        slack,
        message,
        channel=channel,
        username=username,
        emoji=emoji
    )

if __name__ == "__main__":
    msg("Hello World, I'm a fancy Notification Bot!")
