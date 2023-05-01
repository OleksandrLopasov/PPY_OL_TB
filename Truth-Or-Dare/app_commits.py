from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.delete("/dares/{dare_id}")
async def delete_dare(dare_id: int):
    dare_to_delete = session.query(Dare).filter(Dare.idDare == dare_id).first()
    if dare_to_delete:
        session.delete(dare_to_delete)
        session.commit()
        return "Dare deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Dare with id {dare_id} does not exist"
    )


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


@app.get("/packs/")
async def read_packs():
    packs = session.query(Pack).all()
    return packs


@app.post("/packs/")
async def create_pack(pack: Pack):
    session.add(pack)
    session.commit()
    return pack


@app.put("/packs/{pack_id}")
async def update_pack(pack_id: int, pack: Pack):
    pack_to_update = session.query(Pack).filter(Pack.idPack == pack_id).first()
    if pack_to_update:
        if pack.Name:
            pack_to_update.Name = pack.Name
        if pack.idUser:
            pack_to_update.idUser = pack.idUser
        session.commit()
        return pack_to_update
    raise HTTPException(
        status_code=404,
        detail=f"Pack with id {pack_id} does not exist"
    )


@app.delete("/packs/{pack_id}")
async def delete_pack(pack_id: int):
    pack_to_delete = session.query(Pack).filter(Pack.idPack == pack_id).first()
    if pack_to_delete:
        session.delete(pack_to_delete)
        session.commit()
        return "Pack deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Pack with id {pack_id} does not exist"
    )


@app.get("/truths/")
async def read_truths():
    truths = session.query(Truth).all()
    return truths


@app.post("/truths/")
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


@app.get("/users/")
async def read_users():
    users = session.query(User).all()
    return users


@app.post("/users/")
async def create_user(user: User):
    session.add(user)
    session.commit()
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    user_to_update = session.query(User).filter(User.idUser == user_id).first()
    if user_to_update:
        if user.Username:
            user_to_update.Username = user.Username
        if user.Password:
            user_to_update.Password = user.Password
        session.commit()
        return user_to_update
    return "User not found"


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user_to_delete = session.query(User).filter(User.idUser == user_id).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        return "User deleted successfully"
    raise HTTPException(
        status_code=404,
        detail=f"Truth with id {user_id} does not exist"
    )
