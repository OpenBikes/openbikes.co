module.exports = {
  root: true,
  parserOptions: {
    sourceType: 'module'
  },
  extends: 'airbnb-base',
  // required to lint *.vue files
  plugins: [
    'html'
  ],
  // add your custom rules here
  'rules': {
    'func-names': 0,
    'import/no-unresolved': 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    'no-param-reassign': 0,
    'no-console': 0,
    'object-shorthand': 0,
    'space-before-function-paren': 0
  },
  'globals': {
    $: true,
    _: true,
    L: true
  }
}
