require 'spec_helper'
RSpec.describe StringValidator do
  let!(:v) { StringValidator.new }
  it 'exists' do
    expect(v).to be_a StringValidator
  end

  it 'validates an empty string' do
    expect(v.validate("()")).to be true
    expect(v.validate("((")).to be false
    expect(v.validate("([{}[]])")).to be true
  end
end
