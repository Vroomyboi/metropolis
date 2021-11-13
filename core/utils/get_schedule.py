def get_week_schedule_json(user):
    if user.is_authenticated:
        return '{"2021-11-11":[{"description":{"time":"09:00 AM - 11:30 AM","course":"Morning Class"},"time":{"start":"2021-11-11T09:00:00-05:00","end":"2021-11-11T11:30:00-05:00"},"position":[3,6,7],"cycle":"Week 2","course":"SPH3UP-0A"},{"description":{"time":"12:15 PM - 02:45 PM","course":"Afternoon Class"},"time":{"start":"2021-11-11T12:15:00-05:00","end":"2021-11-11T14:45:00-05:00"},"position":[4,6,7],"cycle":"Week 2","course":"SCH3UP-0A"}],"2021-11-12":[{"description":{"time":"09:00 AM - 11:30 AM","course":"Morning Class"},"time":{"start":"2021-11-12T09:00:00-05:00","end":"2021-11-12T11:30:00-05:00"},"position":[3,6,7],"cycle":"Week 2","course":"SPH3UP-0A"},{"description":{"time":"12:15 PM - 02:45 PM","course":"Afternoon Class"},"time":{"start":"2021-11-12T12:15:00-05:00","end":"2021-11-12T14:45:00-05:00"},"position":[4,6,7],"cycle":"Week 2","course":"SCH3UP-0A"}],"2021-11-13":[],"2021-11-14":[],"2021-11-15":[{"description":{"time":"09:00 AM - 11:30 AM","course":"Morning Class"},"time":{"start":"2021-11-15T09:00:00-05:00","end":"2021-11-15T11:30:00-05:00"},"position":[1,5,7],"cycle":"Week 1","course":"PAF3OM-0A"},{"description":{"time":"12:15 PM - 02:45 PM","course":"Afternoon Class"},"time":{"start":"2021-11-15T12:15:00-05:00","end":"2021-11-15T14:45:00-05:00"},"position":[2,5,7],"cycle":"Week 1","course":"MCR3UP-1A"}],"2021-11-16":[{"description":{"time":"09:00 AM - 11:30 AM","course":"Morning Class"},"time":{"start":"2021-11-16T09:00:00-05:00","end":"2021-11-16T11:30:00-05:00"},"position":[1,5,7],"cycle":"Week 1","course":"PAF3OM-0A"},{"description":{"time":"12:15 PM - 02:45 PM","course":"Afternoon Class"},"time":{"start":"2021-11-16T12:15:00-05:00","end":"2021-11-16T14:45:00-05:00"},"position":[2,5,7],"cycle":"Week 1","course":"MCR3UP-1A"}],"2021-11-17":[{"description":{"time":"10:00 AM - 12:00 PM","course":"Morning Class"},"time":{"start":"2021-11-17T10:00:00-05:00","end":"2021-11-17T12:00:00-05:00"},"position":[1,5,7],"cycle":"Week 1","course":"PAF3OM-0A"},{"description":{"time":"12:45 PM - 02:45 PM","course":"Afternoon Class"},"time":{"start":"2021-11-17T12:45:00-05:00","end":"2021-11-17T14:45:00-05:00"},"position":[2,5,7],"cycle":"Week 1","course":"MCR3UP-1A"}]}'
    else:
        return '{}'
