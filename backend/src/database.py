# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import os
# import sys
#
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# from config import Settings
# from typing import Generator
# import logging
#
# logger = logging.getLogger(__name__)
#
# SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL
# logger.info("Database URL is ", SQLALCHEMY_DATABASE_URL)
# engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# def get_db() -> Generator:
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()
