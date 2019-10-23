from server import db
import datetime as dt


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.UnicodeText, nullable=False)
    title = db.Column(db.UnicodeText)
    created_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.UnicodeText, nullable=False)


class Cell(db.Model):
    __tablename__ = 'cell'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cell_type_id = db.Column(db.Integer, db.ForeignKey('cell_type.id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.Integer)

    cell_type = db.relationship("CellType", foreign_keys=[cell_type_id])


class CellType(db.Model):
    __tablename__ = 'cell_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.UnicodeText, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    vendor = db.Column(db.UnicodeText, nullable=False)
    vendor_batch = db.Column(db.UnicodeText, nullable=False)

    electrolyte_id = db.Column(db.Integer, db.ForeignKey('electrolyte.id'),
                            nullable=False)
    positive_electrode_id = db.Column(db.Integer,
                                   db.ForeignKey('positive_electrode.id'),
                                   nullable=False)
    separator_id = db.Column(db.Integer, db.ForeignKey('separator.id'), nullable=False)
    negative_electrode_id = db.Column(db.Integer,
                                   db.ForeignKey('negative_electrode.id'),
                                   nullable=False)

    electrolyte = db.relationship("Electrolyte", foreign_keys=[electrolyte_id])
    positive_electrode = db.relationship("PositiveElectrode",
                                      foreign_keys=[positive_electrode_id])
    separator = db.relationship("Separator", foreign_keys=[separator_id])
    negative_electrode = db.relationship("NegativeElectrode",
                                      foreign_keys=[negative_electrode_id])


class SeparatorComponent(db.Model):
    __tablename__ = 'separator_component'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_date = db.Column(db.DateTime, nullable=False)

    component = db.Column(db.UnicodeText, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)
    smiles = db.Column(db.UnicodeText)


class SeparatorConcentration(db.Model):
    __tablename__ = 'separator_concentration'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    component_id = db.Column(db.Integer, db.ForeignKey('separator_component.id'),
                          nullable=False)
    concentration = db.Column(db.Float, nullable=False)

    component = db.relationship("SeparatorComponent", foreign_keys=[component_id])


class Separator(db.Model):
    __tablename__ = 'separator'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cell_id = db.Column(db.Integer, db.ForeignKey('cell.id'), nullable=False)
    separator_id = db.Column(db.Integer, db.ForeignKey('separator_concentration.id'),
                          nullable=False)

    cell = db.relationship("Cell", foreign_keys=[cell_id])
    separator = db.relationship("SeparatorConcentration",
                             foreign_keys=[separator_id])


class ElectrolyteComponent(db.Model):
    __tablename__ = 'electrolyte_component'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_date = db.Column(db.DateTime, nullable=False)

    component = db.Column(db.UnicodeText, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)
    smiles = db.Column(db.UnicodeText)


class ElectroltyeConcentration(db.Model):
    __tablename__ = 'electrolyte_concentration'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    component_id = db.Column(db.Integer, db.ForeignKey('electrolyte_component.id'),
                          nullable=False)
    concentration = db.Column(db.Float, nullable=False)

    component = db.relationship("ElectrolyteComponent",
                             foreign_keys=[component_id])


class Electrolyte(db.Model):
    __tablename__ = 'electrolyte'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.UnicodeText, nullable=False)
    electrolyte_concentration_id = db.Column(db.Integer,
                            db.ForeignKey('electrolyte_concentration.id'),
                            nullable=False)

    electrolyte_concentration = db.relationship("ElectroltyeConcentration", foreign_keys=[electrolyte_concentration_id])


class ElectrodeComponent(db.Model):
    __tablename__ = 'electrode_component'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_date = db.Column(db.DateTime, nullable=False)

    component = db.Column(db.UnicodeText, nullable=False)
    name = db.Column(db.UnicodeText, nullable=False)
    smiles = db.Column(db.UnicodeText)


class PositiveElectrodeConcentration(db.Model):
    __tablename__ = 'positive_electrode_concentration'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    component_id = db.Column(db.Integer, db.ForeignKey('electrode_component.id'),
                          nullable=False)
    concentration = db.Column(db.Float, nullable=False)

    component = db.relationship("ElectrodeComponent", foreign_keys=[component_id])


class PositiveElectrode(db.Model):
    __tablename__ = 'positive_electrode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cell_id = db.Column(db.Integer, db.ForeignKey('cell.id'), nullable=False)
    positive_electrode_id = db.Column(
            db.Integer,
            db.ForeignKey('positive_electrode_concentration.id'),
            nullable=False)

    cell = db.relationship("Cell", foreign_keys=[cell_id])
    positive_electrode = db.relationship(
            "PositiveElectrodeConcentration",
            foreign_keys=[positive_electrode_id])


class NegativeElectrodeConcentration(db.Model):
    __tablename__ = 'negative_electrode_concentration'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    component_id = db.Column(db.Integer, db.ForeignKey('electrode_component.id'),
                          nullable=False)
    concentration = db.Column(db.Float, nullable=False)

    component = db.relationship("ElectrodeComponent", foreign_keys=[component_id])


class NegativeElectrode(db.Model):
    __tablename__ = 'negative_electrode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cell_id = db.Column(db.Integer, db.ForeignKey('cell.id'), nullable=False)
    positive_electrode_id = db.Column(
            db.Integer,
            db.ForeignKey('negative_electrode_concentration.id'), nullable=False)

    cell = db.relationship("Cell", foreign_keys=[cell_id])
    positive_electrode = db.relationship(
            "NegativeElectrodeConcentration",
            foreign_keys=[positive_electrode_id])


class MeasurementType(db.Model):
    __tablename__ = 'measurement_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.UnicodeText, nullable=False)
    table_name = db.Column(db.String(32), nullable=False)


class Measurement(db.Model):
    __tablename__ = 'measurement'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    cell_id = db.Column(db.Integer, db.ForeignKey('cell.id'), nullable=False)
    measurement_type_id = db.Column(db.Integer, db.ForeignKey('measurement_type.id'),
                                 nullable=False)

    project = db.relationship("Project", foreign_keys=[project_id])
    cell = db.relationship('Cell', foreign_keys=[cell_id])
    measurement_type = db.relationship('MeasurementType',
                                    foreign_keys=[measurement_type_id])


class VirtualProject(db.Model):
    __tablename__ = 'virtual_project'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.UnicodeText, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.UnicodeText, nullable=False)


class VirtualProjectCatalog(db.Model):
    __tablename__ = 'virtual_project_catalog'

    virtual_project_id = db.Column(db.Integer, db.ForeignKey('virtual_project.id'),
                                nullable=False, primary_key=True)
    measurement_id = db.Column(db.Integer, db.ForeignKey('measurement.id'),
                            nullable=False, primary_key=True)

    measurement = db.relationship('Measurement', foreign_keys=[measurement_id])


class CyclerInstrument(db.Model):
    __tablename__ = 'cycler_instrument'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    model = db.Column(db.String(32), nullable=False)


class Cycling(db.Model):
    __tablename__ = 'cycling'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    cell_id = db.Column(db.Integer, db.ForeignKey('cell.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    temperature_K = db.Column(db.Float)
    data_table_name = db.Column(db.String(32), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    raw_data__filename = db.Column(db.String(32))
    cycler_instrument_id = db.Column(
            db.Integer,
            db.ForeignKey('cycler_instrument.id'), nullable=False)


def create_cycling_data_table(data_table_name):
    table = db.Table(
        data_table_name,
        db.Column('date_time', db.DateTime, nullable=False),
        db.Column('test_time', db.Float, nullable=False),
        db.Column('step_time', db.Float, nullable=False),
        db.Column('step_index', db.Integer, nullable=False),
        db.Column('cycle_index', db.Integer, nullable=False),
        db.Column('current_A', db.Float, nullable=False),
        db.Column('voltage_V', db.Float, nullable=False)
        )
    return table
