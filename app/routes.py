from flask import Blueprint, request, jsonify
from app import db
from app.models import Member
from app.schemas import member_schema, members_schema

members_bp = Blueprint("members", __name__, url_prefix="/members")

@members_bp.route("/", methods=["POST"])
def create_member():
    member = member_schema.load(request.json)
    db.session.add(member)
    db.session.commit()
    return member_schema.dump(member), 201

@members_bp.route("/", methods=["GET"])
def get_members():
    members = Member.query.all()
    return members_schema.dump(members), 200
