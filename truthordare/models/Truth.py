from truthordare.utils import *


metadata = MetaData()
mapper_registry = registry(metadata=metadata)


@mapper_registry.mapped_as_dataclass
class Truth:
    __tablename__ = "Truth"

    id_truth: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255))
    id_pack: Mapped[int] = mapped_column(ForeignKey("Pack.id_pack"))

    packs: Mapped["Pack"] = relationship(
        "Pack", secondary="Truth_Pack", back_populates="truths", cascade="all, delete-orphan"
    )


@mapper_registry.mapped_as_dataclass
class Truth_Pack:
    __tablename__ = "Truth_Pack"

    id_pack: Mapped[int] = mapped_column(Integer, ForeignKey("Pack.id_pack"), primary_key=True)
    id_truth: Mapped[int] = mapped_column(Integer, ForeignKey("Truth.id_truth", primary_key=True))


metadata.create_all(bind=connection.engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=connection.engine)

session = SessionLocal()
app = FastAPI()


@app.get("/truths/")
async def read_truths():
    truths = session.query(Truth).all()
    return truths


@app.post("/truths/addTruth")
async def create_truth(truth: Truth):
    session.add(truth)
    session.commit()
    return truth


@app.put("/truths/{truth_id}")
async def update_truth(truth_id: int, truth: Truth):
    truth_to_update = session.query(Truth).filter(Truth.idTruth == truth_id).first()
    if truth_to_update:
        if truth.Text:
            truth_to_update.Text = truth.Text
        session.commit()
        return truth_to_update
    return "Truth not found"


@app.delete("/truths/{truth_id}")
async def delete_truth(truth_id: int):
    truth_to_delete = session.query(Truth).filter(Truth.idTruth == truth_id).first()
    if truth_to_delete:
        session.delete(truth_to_delete)
        session.commit()
        return "Truth deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Truth with id {truth_id} does not exist"
    )
