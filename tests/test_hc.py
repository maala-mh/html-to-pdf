def test_hc(client):
    res = client.get("/hc").json()
    assert res["message"] == "OK", "hc failed"
