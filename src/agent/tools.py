from langchain_core.tools import tool
from datetime import datetime

# SMART LIGHTS TOOLS
@tool
def turn_on_light(room: str, brightness: int = 100) -> str:
    """Turn on smart light in a specific room with optional brightness level (0-100)."""
    return f"Light in {room} turned ON with brightness {brightness}%"

@tool
def turn_off_light(room: str) -> str:
    """Turn off smart light in a specific room."""
    return f"Light in {room} turned OFF"

@tool
def dim_light(room: str, brightness: int) -> str:
    """Dim smart light in a specific room to a specific brightness level (0-100)."""
    return f"Light in {room} dimmed to {brightness}%"

@tool
def set_light_color(room: str, color: str) -> str:
    """Set the color of smart light in a specific room."""
    return f"Light in {room} color changed to {color}"

@tool
def turn_on_all_lights() -> str:
    """Turn on all smart lights in the house."""
    return "All lights in the house turned ON"

@tool
def turn_off_all_lights() -> str:
    """Turn off all smart lights in the house."""
    return "All lights in the house turned OFF"

# THERMOSTAT TOOLS
@tool
def set_thermostat_temperature(temperature: int, unit: str = "celsius") -> str:
    """Set the thermostat to a specific temperature."""
    return f"Thermostat set to {temperature}°{unit[0].upper()}"

@tool
def get_current_temperature() -> str:
    """Get the current temperature reading from the thermostat."""
    return "Current temperature: 22°C (72°F)"

@tool
def set_thermostat_mode(mode: str) -> str:
    """Set thermostat mode: heating, cooling, auto, or off."""
    return f"Thermostat mode set to {mode}"

@tool
def schedule_temperature(time: str, temperature: int, unit: str = "celsius") -> str:
    """Schedule temperature change at a specific time."""
    return f"Temperature scheduled to {temperature}°{unit[0].upper()} at {time}"

# DOOR LOCK TOOLS
@tool
def lock_door(door_name: str) -> str:
    """Lock a specific smart door."""
    return f"{door_name} door locked successfully"

@tool
def unlock_door(door_name: str) -> str:
    """Unlock a specific smart door."""
    return f"{door_name} door unlocked successfully"

@tool
def check_door_status(door_name: str) -> str:
    """Check if a specific door is locked or unlocked."""
    return f"{door_name} door status: LOCKED"

@tool
def lock_all_doors() -> str:
    """Lock all smart doors in the house."""
    return "All doors locked successfully"

@tool
def unlock_all_doors() -> str:
    """Unlock all smart doors in the house."""
    return "All doors unlocked successfully"

# SECURITY CAMERA TOOLS
@tool
def get_camera_snapshot(camera_location: str) -> str:
    """Get a snapshot from a security camera at a specific location."""
    return f"Snapshot captured from {camera_location} camera at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

@tool
def start_camera_recording(camera_location: str, duration: int = 60) -> str:
    """Start recording from a security camera for specified duration in seconds."""
    return f"Recording started on {camera_location} camera for {duration} seconds"

@tool
def check_motion_detection(camera_location: str) -> str:
    """Check motion detection status for a specific camera."""
    return f"Motion detection on {camera_location} camera: ACTIVE - No motion detected in last 5 minutes"

@tool
def enable_night_vision(camera_location: str) -> str:
    """Enable night vision mode for a specific camera."""
    return f"Night vision enabled for {camera_location} camera"

# PLANT WATERING TOOLS
@tool
def water_plants(zone: str, duration: int = 30) -> str:
    """Water plants in a specific zone for specified duration in seconds."""
    return f"Watering plants in {zone} for {duration} seconds"

@tool
def check_soil_moisture(zone: str) -> str:
    """Check soil moisture level in a specific plant zone."""
    return f"Soil moisture in {zone}: 65% - Adequate"

@tool
def set_watering_schedule(zone: str, time: str, duration: int = 30) -> str:
    """Set automatic watering schedule for a plant zone."""
    return f"Watering schedule set for {zone}: {time} daily for {duration} seconds"

@tool
def get_plant_care_reminder(plant_type: str) -> str:
    """Get care reminder for a specific type of plant."""
    return f"{plant_type} care reminder: Water when soil is dry, provide indirect sunlight"

# ADDITIONAL SMART HOME TOOLS
@tool
def set_window_blinds(room: str, position: int) -> str:
    """Set window blinds position (0-100%) in a specific room."""
    return f"Window blinds in {room} set to {position}% open"

@tool
def start_smart_vacuum(room: str = "all") -> str:
    """Start smart vacuum cleaner in a specific room or entire house."""
    return f"Smart vacuum started cleaning {room}"

@tool
def play_music(room: str, playlist: str = "default") -> str:
    """Play music in a specific room with optional playlist."""
    return f"Playing {playlist} playlist in {room}"

@tool
def set_alarm(time: str, message: str = "Wake up!") -> str:
    """Set an alarm for a specific time with optional message."""
    return f"Alarm set for {time} with message: '{message}'"

@tool
def check_air_quality() -> str:
    """Check indoor air quality readings."""
    return "Air Quality: Good - PM2.5: 15 μg/m³, Humidity: 45%, CO2: 420 ppm"

@tool
def control_smart_fan(room: str, speed: int, action: str = "on") -> str:
    """Control smart fan - turn on/off and set speed (1-5)."""
    if action == "off":
        return f"Smart fan in {room} turned OFF"
    return f"Smart fan in {room} turned ON at speed level {speed}"

# Get all tools for easy export
HOME_AUTOMATION_TOOLS = [
    turn_on_light, turn_off_light, dim_light, set_light_color, turn_on_all_lights, turn_off_all_lights,
    set_thermostat_temperature, get_current_temperature, set_thermostat_mode, schedule_temperature,
    lock_door, unlock_door, check_door_status, lock_all_doors, unlock_all_doors,
    get_camera_snapshot, start_camera_recording, check_motion_detection, enable_night_vision,
    water_plants, check_soil_moisture, set_watering_schedule, get_plant_care_reminder,
    set_window_blinds, start_smart_vacuum, play_music, set_alarm, check_air_quality, control_smart_fan
] 