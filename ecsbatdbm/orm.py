from sqlalchemy import Column, ForeignKey, Float, \
    Integer, String, UnicodeText, DateTime, create_engine, metadata
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()
metadata = MetaData()

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(UnicodeText, nullable=False)
    created_date = Column(DateTime, nullable=False)
    description = Column(UnicodeText, nullable=False)


class Cell(Base):
    __tablename__ = 'cell'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cell_type_id = Column(Integer, ForeignKey('cell_type.id'), nullable=False)
    created_date = Column(DateTime, nullable=False)

    cell_type = relationship("CellType", foreign_keys=[cell_type_id])


class CellType(Base):
    __tablename__ = 'cell_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(UnicodeText, nullable=False)
    created_date = Column(DateTime, nullable=False)
    vendor = Column(UnicodeText, nullable=False)
    vendor_batch = Column(UnicodeText, nullable=False)

    electrolyte_id = Column(Integer, ForeignKey('electrolyte.id'),
                            nullable=False)
    positive_electrode_id = Column(Integer,
                                   ForeignKey('positive_electrode.id'),
                                   nullable=False)
    separator_id = Column(Integer, ForeignKey('separator.id'), nullable=False)
    negative_electrode_id = Column(Integer,
                                   ForeignKey('negative_electrode.id'),
                                   nullable=False)

    electrolyte = relationship("Electrolyte", foreign_keys=[electrolyte_id])
    positive_electrode = relationship("PositiveElectrode",
                                      foreign_keys=[positive_electrode_id])
    separator = relationship("Separator", foreign_keys=[separator_id])
    negative_electrode = relationship("NegativeElectrode",
                                      foreign_keys=[negative_electrode_id])


class SeparatorComponent(Base):
    __tablename__ = 'separator_component'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, nullable=False)

    component = Column(UnicodeText, nullable=False)
    name = Column(UnicodeText, nullable=False)
    smiles = Column(UnicodeText)


class SeparatorConcentration(Base):
    __tablename__ = 'separator_concentration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    component_id = Column(Integer, ForeignKey('separator_component.id'),
                          nullable=False)
    concentration = Column(Float, nullable=False)

    component = relationship("SeparatorComponent", foreign_keys=[component_id])


class Separator(Base):
    __tablename__ = 'separator'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cell_id = Column(Integer, ForeignKey('cell.id'), nullable=False)
    separator_id = Column(Integer, ForeignKey('separator_concentration.id'),
                          nullable=False)

    cell = relationship("Cell", foreign_keys=[cell_id])
    separator = relationship("SeparatorConcentration",
                             foreign_keys=[separator_id])


class ElectrolyteComponent(Base):
    __tablename__ = 'electrolyte_component'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, nullable=False)

    component = Column(UnicodeText, nullable=False)
    name = Column(UnicodeText, nullable=False)
    smiles = Column(UnicodeText)


class ElectroltyeConcentration(Base):
    __tablename__ = 'electrolyte_concentration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    component_id = Column(Integer, ForeignKey('electrolyte_component.id'),
                          nullable=False)
    concentration = Column(Float, nullable=False)

    component = relationship("ElectrolyteComponent",
                             foreign_keys=[component_id])


class Electrolyte(Base):
    __tablename__ = 'electrolyte'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cell_id = Column(Integer, ForeignKey('cell.id'), nullable=False)
    electrolyte_id = Column(Integer,
                            ForeignKey('electrolyte_concentration.id'),
                            nullable=False)

    cell = relationship("Cell", foreign_keys=[cell_id])
    electrolyte = relationship("ElectroltyeConcentration",
                               foreign_keys=[electrolyte_id])


class ElectrodeComponent(Base):
    __tablename__ = 'electrode_component'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, nullable=False)

    component = Column(UnicodeText, nullable=False)
    name = Column(UnicodeText, nullable=False)
    smiles = Column(UnicodeText)


class PositiveElectrodeConcentration(Base):
    __tablename__ = 'positive_electrode_concentration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    component_id = Column(Integer, ForeignKey('electrode_component.id'),
                          nullable=False)
    concentration = Column(Float, nullable=False)

    component = relationship("ElectrodeComponent", foreign_keys=[component_id])


class PositiveElectrode(Base):
    __tablename__ = 'positive_electrode'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cell_id = Column(Integer, ForeignKey('cell.id'), nullable=False)
    positive_electrode_id = Column(
            Integer,
            ForeignKey('positive_electrode_concentration.id'),
            nullable=False)

    cell = relationship("Cell", foreign_keys=[cell_id])
    positive_electrode = relationship(
            "PositiveElectrodeConcentration",
            foreign_keys=[positive_electrode_id])


class NegativeElectrodeConcentration(Base):
    __tablename__ = 'negative_electrode_concentration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    component_id = Column(Integer, ForeignKey('electrode_component.id'),
                          nullable=False)
    concentration = Column(Float, nullable=False)

    component = relationship("ElectrodeComponent", foreign_keys=[component_id])


class NegativeElectrode(Base):
    __tablename__ = 'negative_electrode'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cell_id = Column(Integer, ForeignKey('cell.id'), nullable=False)
    positive_electrode_id = Column(
            Integer,
            ForeignKey('negative_electrode_concentration.id'), nullable=False)

    cell = relationship("Cell", foreign_keys=[cell_id])
    positive_electrode = relationship(
            "NegativeElectrodeConcentration",
            foreign_keys=[positive_electrode_id])


class MeasurementType(Base):
    __tablename__ = 'measurement_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(UnicodeText, nullable=False)
    table_name = Column(String(32), nullable=False)


class Measurement(Base):
    __tablename__ = 'measurement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    cell_id = Column(Integer, ForeignKey('cell.id'), nullable=False)
    measurement_type_id = Column(Integer, ForeignKey('measurement_type.id'),
                                 nullable=False)

    project = relationship("Project", foreign_keys=[project_id])
    cell = relationship('Cell', foreign_keys=[cell_id])
    measurement_type = relationship('MeasurementType',
                                    foreign_keys=[measurement_type_id])


class VirtualProject(Base):
    __tablename__ = 'virtual_project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(UnicodeText, nullable=False)
    created_date = Column(DateTime, nullable=False)
    description = Column(UnicodeText, nullable=False)


class VirtualProjectCatalog(Base):
    __tablename__ = 'virtual_project_catalog'

    virtual_project_id = Column(Integer, ForeignKey('virtual_project.id'),
                                nullable=False, primary_key=True)
    measurement_id = Column(Integer, ForeignKey('measurement.id'),
                            nullable=False, primary_key=True)

    measurement = relationship('Measurement', foreign_keys=[measurement_id])


class CyclerInstrument(Base):
    __tablename__ = 'cycler_instrument'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    model = Column(String(32), nullable=False)


class Cycling(Base):
    __tablename__ = 'cycling'

    id = Column(Integer, primary_key=True, autoincrement=True)

    cell_id = Column(Integer, ForeignKey('cell.id'), nullable=False)
    project_id = Column(Integer, ForeignKey('project.id'), nullable=False)
    temperature_K = Column(Float)
    data_table_name = Column(String(32), nullable=False)
    created_date = Column(DateTime, nullable=False)
    raw_data__filename = Column(String(32))
    cycler_instrument_id = Column(
            Integer,
            ForeignKey('cycler_instrument.id'), nullable=False)


def create_cycling_data_table(data_table_name):
    table = Table(
        data_table_name, metadata,
        Column('date_time', DateTime, nullable=False),
        Column('test_time', Float, nullable=False),
        Column('step_time', Float, nullable=False),
        Column('step_index', Integer, nullable=False),
        Column('cycle_index', Integer, nullable=False),
        Column('current_A', Float, nullable=False),
        Column('voltage_V', Float, nullable=False)
        )

def create_sqlite3(db_out_filename):
    url = 'sqlite:///' + db_out_filename
    db = create_engine(url)
    con = db.connect()
    Base.metadata.create_all(db)
    con.close()
