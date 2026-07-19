# Notes:
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    active_events: list[int | str] = list(range(1, 14 + 1))

    i = 1  # ==== overdrive1 ====
    if i in active_events:
        event_name = f"overdrive{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(36.5713867, 136.6544585),
                address="14-31 Musashimachi, Kanazawa, Ishikawa 920-0855, Japan",
                description="石川県金沢市武蔵町14番31号ITビジネスプラザ武蔵　6F交流室",
                sources=[
                    Source(
                        "https://www.pixiv.net/event_detail.php?event_id=676",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=2FSBs1hD8xg_CjyFnQAH_w&w=1177&h=580&thumb=2&yaw=136.62485&pitch=0",
                url="https://maps.app.goo.gl/1FcJLuPW7FMkz5gw5",
            ),
        ]
        event = Event(
            aliases=["OVERDRIVE!!", "OVERDRIVE"],
            dates="2010.11.07",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130710182714/http://slash.sakuraweb.com/event/archive/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participjating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            # description=None,
            comments="Participating circles dead: https://web.archive.org/web/20130710182714/http://slash.sakuraweb.com/event/archive/\nPerhaps could be found here, but I won't bother: https://web.archive.org/web/*/http://neko2.net/*",
            last_edited="2026.06.20",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== overdrive2 ====
    if i in active_events:
        event_name = f"overdrive{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "02_20110811024331_top4.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20111006170202/http://slash.sakuraweb.com/event/vo_sta/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
            Medium(
                "02_20110811024331_banner.gif",
                [
                    Source(
                        "https://web.archive.org/web/20111006170202/http://slash.sakuraweb.com/event/vo_sta/",
                        (RT.Reliable, OT.Official),
                    )
                ],
            ),
        ]
        locations = [
            Location(
                coordinates=(36.5713867, 136.6544585),
                address="14-31 Musashimachi, Kanazawa, Ishikawa 920-0855, Japan",
                description="石川県金沢市武蔵町14-31ITビジネスプラザ武蔵5F・6F",
                sources=[
                    Source(
                        "https://www.pixiv.net/event_detail.php?event_id=1231",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://streetviewpixels-pa.googleapis.com/v1/thumbnail?output=thumbnail&cb_client=maps_sv.tactile.gps&panoid=2FSBs1hD8xg_CjyFnQAH_w&w=1177&h=580&thumb=2&yaw=136.62485&pitch=0",
                url="https://maps.app.goo.gl/1FcJLuPW7FMkz5gw5",
            ),
        ]
        event = Event(
            aliases=["OVERDRIVE!! SECOND", "OVERDRIVE SECOND"],
            dates="2010.10.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20110820081315/http://slash.sakuraweb.com/event/about.htm",
                    (RT.Reliable, OT.Official),
                ),
                Source("Participating circles: https://web.archive.org/web/20130710182339/http://slash.sakuraweb.com/event/circlelist.htm", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            # description=None,
            comments="Simultaneous with VOCALOID STATION",
            last_edited="2026.06.20",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # ==== event group ====
    media = [
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
        # Medium("",
        #        [Source("", (RT.Reliable, OT.Official))]),
    ]
    links = [
        "http://neko2.net/overdrive/",
        "https://web.archive.org/web/20110811024331/http://slash.sakuraweb.com/event/",
        "https://x.com/slash_event",
    ]

    event_group = EventGroup(
        aliases=["OVERDRIVE!!", "OVERDRIVE"],
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description=None,
        last_edited="2026.06.20",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
