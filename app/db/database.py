from fastapi import FastAPI, HTTPException, Depends, Query
from sqlmodel import Field, SQLModel, Session, create_engine, select
from typing import Annotated
