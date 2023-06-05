@app.get("/dare-packs/")
async def read_dare_packs():
    dare_packs = session.query(Dare_Pack).all()
    return dare_packs


@app.post("/dare-packs/")
async def create_dare_pack(dare_pack: Dare_Pack):
    session.add(dare_pack)
    session.commit()
    return dare_pack


@app.put("/dare-packs/{dare_id}/{pack_id}")
async def update_dare_pack(dare_id: int, pack_id: int, dare_pack: Dare_Pack):
    dare_pack_to_update = session.query(Dare_Pack).filter(Dare_Pack.idDare == dare_id, Dare_Pack.idPack == pack_id).first()
    if dare_pack_to_update:
        if dare_pack.idDare:
            dare_pack_to_update.idDare = dare_pack.idDare
        if dare_pack.idPack:
            dare_pack_to_update.idPack = dare_pack.idPack
        session.commit()
        return dare_pack_to_update
    raise HTTPException(
        status_code=404,
        detail=f"Dare with id {dare_id} does not exist"
    )


@app.delete("/dare-packs/{dare_id}/{pack_id}")
async def delete_dare_pack(dare_id: int, pack_id: int):
    dare_pack_to_delete = session.query(Dare_Pack).filter(Dare_Pack.idDare == dare_id, Dare_Pack.idPack == pack_id).first()
    if dare_pack_to_delete:
        session.delete(dare_pack_to_delete)
        session.commit()
        return "Dare pack deleted successfully"
    return "Dare pack not found"

@app.get("/truth-packs/")
async def read_truth_packs():
    truth_packs = session.query(Truth_Pack).all()
    return truth_packs


@app.post("/truth-packs/")
async def create_truth_pack(truth_pack: Truth_Pack):
    session.add(truth_pack)
    session.commit()
    return truth_pack


@app.put("/truth-packs/{truth_id}/{pack_id}")
async def update_truth_pack(truth_id: int, pack_id: int, truth_pack: Truth_Pack):
    truth_pack_to_update = session.query(Truth_Pack).filter(Truth_Pack.idTruth == truth_id, Truth_Pack.idPack == pack_id).first()
    if truth_pack_to_update:
        if truth_pack.idTruth:
            truth_pack_to_update.idTruth = truth_pack.idTruth
        if truth_pack.idPack:
            truth_pack_to_update.idPack = truth_pack.idPack
        session.commit()
        return truth_pack_to_update
    return "Truth pack not found"


@app.delete("/truth-packs/{truth_id}/{pack_id}")
async def delete_truth_pack(truth_id: int, pack_id: int):
    truth_pack_to_delete = session.query(Truth_Pack).filter(Truth_Pack.idTruth == truth_id, Truth_Pack.idPack == pack_id).first()
    if truth_pack_to_delete:
        session.delete(truth_pack_to_delete)
        session.commit()
        return "Truth pack deleted successfully"
    return "Truth pack not found"

