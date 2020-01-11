import datetime
from unittest.mock import call

import pytest

from todolist.task import Task, ToDo


def test_base():
    assert True


def test_task_create_simple_object():
    now = datetime.datetime.utcnow()
    task = Task("Posprzataj", 5, now)

    assert task.getDescription() == "Posprzataj"
    assert task.getPiority() == 5
    assert task.getDate() == now


def test_task_create_simple2_object():
    task = Task("Wyprowadz psa", 3)

    assert task.getDescription() == "Wyprowadz psa"
    assert task.getPiority() == 3
    assert task.getFinish() is False


def test_todo_add_task_to_todo():
    todo = ToDo()
    task = Task("Nakarm psa", 3)
    todo.add(task)

    assert todo.getTasks() == [task]


def test_todo_add_task_to_todo():
    todo = ToDo()
    task2 = Task("Nakarm psa", 3)
    task1 = Task("Nakarm kota", 3)
    todo.add(task1)
    task2.setFinish(True)
    todo.add(task2)

    assert todo.getFinishTasks() == [task2]


def test_todo_check_today_tasks(create_task, mocker):
    todo = ToDo()
    mock_task1 = mocker.Mock()
    mock_task1.getDate.return_value = datetime.datetime.utcnow()
    desc = mock_task1.getDescription()
    #task1 = Task("Nakarm psa", 3 , datetime.datetime.utcnow())
    task2 = Task("Nakarm kota", 3, datetime.datetime.utcnow()-datetime.timedelta(days=1))
    task3 = create_task
    todo.add(mock_task1)
    todo.add(task2)
    todo.add(task3)

    assert todo.getTodayTasks() == [mock_task1, task3]
    assert mock_task1.getDate.call_count == 3



def test_write_to_file(create_file_desc):
    todo = ToDo()
    task1 = Task("Nakarm psa", 3, datetime.datetime.utcnow())
    todo.add(task1)

    todo.write(create_file_desc)


    file = open('file.txt', 'r+')
    assert file.readline() == "Nakarm psa"

@pytest.fixture
def create_task():
    yield Task("Nakarm konia", 3, datetime.datetime.utcnow())

@pytest.fixture()
def create_file_desc():
    f = open("file.txt", "w+")
    yield f
    f.close()


@pytest.fixture()
def create_mock(mocker):
    mock_task1 = mocker.Mock()
    mock_task1.getDate.return_value = datetime.datetime.utcnow()
    yield mock_task1


