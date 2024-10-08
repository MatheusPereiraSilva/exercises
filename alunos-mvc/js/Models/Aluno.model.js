class AlunoModel {
  // constructor(aluno){
  //   this.nome = aluno.nome
  // }
  constructor({ nome, _id, notas } = { notas: {} }) {
    this.nome = nome;
    this._id = _id !== undefined ? _id : this.generateId();
    this.notas = {...notas};
    if (this._id > AlunoModel.maxId) {
      AlunoModel.maxId = this._id;
    }
    this.media = {};
    this.generateAverage();
  }
  generateId() {
    return AlunoModel.maxId + 1;
  }
  generateAverage(){
    for (let materia in this.notas) {
      this.media[materia] = average(...this.notas[materia]);
    }
  }
}
AlunoModel.maxId = 0;
