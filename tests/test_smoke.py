def test_smoke():
    from lambdawalker.template.fields import field_generators
    from lambdawalker.template.server.TemplateServer import TemplateServer
    from lambdawalker.template.render.CardRenderer import CardRenderer
    assert field_generators is not None
    assert TemplateServer is not None
    assert CardRenderer is not None
    print("template OK")
