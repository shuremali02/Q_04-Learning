from agents import function_tool

@function_tool
def get_weather(location: str, time: str):
    """
    Returns the weather forecast for a given location and time.
    Args:
        location (str): The city or place name.
        time (str): The time (e.g., 'tomorrow afternoon').
    """
    return f"The weather in {location} at {time} will be sunny with temperatures around 30°C."

@function_tool
def find_restaurant(cuisine: str, location: str, open_now: bool):
    """
    Finds restaurants by cuisine and location.
    Args:
        cuisine (str): Type of food (e.g., 'Chinese').
        location (str): Area or city.
        open_now (bool): Whether to filter for currently open places.
    """
    return f"Found 3 {cuisine} restaurants in {location} that are currently {'open' if open_now else 'closed'}."

@function_tool
def send_email(to: str, subject: str, content: str):
    """
    Sends an email with subject and content.
    Args:
        to (str): Recipient name or email.
        subject (str): Email subject.
        content (str): Email body.
    """
    return f"Email sent to {to} with subject '{subject}' and content: {content}"

@function_tool
def schedule_meeting(title: str, time: str, participants: list):
    """
    Schedules a meeting.
    Args:
        title (str): Title of the meeting.
        time (str): Date and time.
        participants (list): List of participants.
    """
    return f"Meeting titled '{title}' scheduled for {time} with participants: {', '.join(participants)}."

@function_tool
def search_product(category: str, budget: float, features: list):
    """
    Searches products in a category within budget and with desired features.
    Args:
        category (str): Product type.
        budget (float): Maximum budget.
        features (list): List of desired features.
    """
    return f"Found wireless Bluetooth headphones under ${budget} with features: {', '.join(features)}."