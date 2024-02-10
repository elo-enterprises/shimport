## API for 'shimport' package

---------------------------------------------------------------------------------------------------------------------------------------------------------------
### shimport
* Overview:  [source code](/src/shimport/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
-------------------------------------------------------------------------------
### shimport.hooks
* Overview:  [source code](/src/shimport/hooks.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shimport.abcs
* Overview:  [source code](/src/shimport/abcs/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`shimport.abcs.FilterResult`](/src/shimport/abcs/__init__.py#L10-L33)
    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)
* Classes: (1 total)
  * [`shimport.abcs.FilterResult`](/src/shimport/abcs/__init__.py#L10-L33)
    * with bases ([`__builtin__.list`](https://docs.python.org/3/library/functions.html#list),[Generic](#typing),)
-------------------------------------------------------------------------------
### shimport.abcs.attrdict
* Overview:  [source code](/src/shimport/abcs/attrdict.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`shimport.abcs.attrdict.AttrDictBase`](/src/shimport/abcs/attrdict.py#L9-L49)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
  * [`shimport.abcs.attrdict.AttrDict`](/src/shimport/abcs/attrdict.py#L55-L56)
    * with bases ([AttrDictBase](#shimportabcsattrdict),[`__builtin__.dict`](https://docs.python.org/3/library/functions.html#dict),)
-------------------------------------------------------------------------------
### shimport.models
* Overview:  [source code](/src/shimport/models.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (2 total)
  * [`shimport.models.ModulesWrapper`](/src/shimport/models.py#L23-L381)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
    * with admonitions:  [🐉 Complex](/src/shimport/models.py#L192 "score 8 / 7")  [🐉 Complex](/src/shimport/models.py#L224 "score 12 / 7") 
    * with properties: (3 total)
      *  [`module`](/src/shimport/models.py#L92) -> inspect._empty
      *  [`parent`](/src/shimport/models.py#L111) -> inspect._empty
      *  [`parent_folder`](/src/shimport/models.py#L106) -> inspect._empty
  * [`shimport.models.LazyModule`](/src/shimport/models.py#L384-L415)
    * with bases ([`__builtin__.object`](https://docs.python.org/3/library/functions.html#object),)
-------------------------------------------------------------------------------
### shimport.importing
* Overview:  [source code](/src/shimport/importing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shimport._version
* Overview:  [source code](/src/shimport/_version.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shimport.registry
* Overview:  [source code](/src/shimport/registry.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shimport.constants
* Overview:  [source code](/src/shimport/constants.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shimport.types
* Overview:  [source code](/src/shimport/types.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
-------------------------------------------------------------------------------
### shimport.module
* Overview:  [source code](/src/shimport/module.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (1 total)
  * [`shimport.module.ModuleBuilder`](/src/shimport/module.py#L10-L46)
    * with bases ([ModulesWrapper](#shimportmodels),)
    * with properties: (3 total)
      *  [`module`](/src/shimport/module.py#L92) -> inspect._empty
      *  [`parent`](/src/shimport/module.py#L111) -> inspect._empty
      *  [`parent_folder`](/src/shimport/module.py#L106) -> inspect._empty
* Functions: (3 total)
  * [`shimport.module.lazy`](/src/shimport/module.py#L103-L113) with signature `(module_name: str) -> shimport.models.LazyModule`
  * [`shimport.module.module_builder`](/src/shimport/module.py#L49-L75)
    * with signature `(name: str, return_objects=False, assign_objects: bool = True, sort_objects: Dict = {}, **kwargs) -> None`
  * [`shimport.module.wrap`](/src/shimport/module.py#L82-L97) with signature `(name, **kwargs)`
-------------------------------------------------------------------------------
### shimport.util
* Overview:  [source code](/src/shimport/util/__init__.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Classes: (0 total)
* Functions: (1 total)
  * [`shimport.util.get_namespace`](/src/shimport/util/__init__.py#L8-L25) with signature `(name)`
-------------------------------------------------------------------------------
### shimport.util.typing
* Overview:  [source code](/src/shimport/util/typing.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`shimport.util.typing.is_subclass`](/src/shimport/util/typing.py#L23-L29) with signature `(x, y, strict=True)`
  * [`shimport.util.typing.new_in_class`](/src/shimport/util/typing.py#L14-L20) with signature `(name: str, kls: Type)`
-------------------------------------------------------------------------------
### shimport.util.lme
* Overview:  [source code](/src/shimport/util/lme.py), [unit tests](/tests/units/), [integration tests](/tests/integrations/)
* Functions: (2 total)
  * [`shimport.util.lme.get_logger`](/src/shimport/util/lme.py#L24-L50)
    * with signature `(name, console=<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>)`
  * [`shimport.util.lme.set_global_level`](/src/shimport/util/lme.py#L9-L18) with signature `(level)`
