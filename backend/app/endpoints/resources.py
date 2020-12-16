from fastapi import APIRouter, Depends, HTTPException
from app.db import users
from app.db import members
from app.helpers.deps import get_current_user

router = APIRouter()


@router.get('/users')
def get_users(user=Depends(get_current_user)):
    """
    Return the users only if the user has been granted with user scope
     :return: all the users
    """
    groups = user.get('groups')
    if 'users' not in groups:
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to view the users"
        )
    
    return users.get_all_users()


@router.get('/members')
def get_members(user=Depends(get_current_user)):
    """
    Return the profiles only if the user has been granted with user scope
    :return: all the members
    """
    groups = user.get('groups')
    if 'members' not in groups:
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to view the members"
        )
    
    return members.get_all_members()
