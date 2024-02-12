from rentomatic.responses import ResponsesSuccess


def room_list_use_case(repo, request):
    rooms = repo.list()
    return ResponseSuccess(rooms)
