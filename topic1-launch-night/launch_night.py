game_services = [
    {"name": "Login Service", "status": "online"},
    {"name": "Realm Server", "status": "online"},
    {"name": "Auction House", "status": "offline"},
    {"name": "In-game Mail", "status": "online"}
]

def warning():
    """Display a warning message if any services are offline."""
    offline_services = count_offline_services(game_services)
    if offline_services > 0:
        print("\nWARNING: Some services are offline!")

def display_services(services):
    """Display the name and status of every game service."""
    for service in services:
        print(f"{service['name']}: {service['status']}")


def count_offline_services(services):
    """Count and return the number of offline services."""
    # TODO: Replace the line below by following Stage 6 in README.md.
    offline_count = 0

    for service in services:
        if service["status"] == "offline":
            offline_count += 1

    return offline_count


print("LAUNCH NIGHT SERVICE MONITOR")
print("=" * 28)

display_services(game_services)
warning()

offline_services = count_offline_services(game_services)
print(f"\nOffline services: {offline_services}")
